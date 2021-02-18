#!/usr/bin/env python3

"""
Copies over and transforms markdown files from a personal journal directory.
Only copies files with `blog: true` in their frontmatter.


Usage:
./blog.py \
    --target="/path/to/blog/repo"    # (optional) Where Hugo files are. Defaults to current directory.
    --source="/path/to/personal/notes"  # (optional) Where markdown files are. Defaults to current directory.
    --clean=false  # (optional) If true, will erase target directories and re-copy all blog files.
    --nofail=false  # (optional) If true, script will quit when exception is thrown during file copying. If false, error'ed files are skipped.

Run `chmod +x blog.py` to make this file executable.
Make sure python fire is installed in python3 using `pip3 install fire`.
See https://github.com/google/python-fire


Feature wishlist:
- Auto-publish: prompt user with diff, then commit and push, then hugo build and push site.
- Include backlinks from other blog posts.
- Make file edits available to hugo.
"""

import fire
import yaml
import os
import os.path
import glob
import copy
import datetime
import re
import time
import shutil


LOG_FILE = 'blog.yaml'

# Whether to copy over posts marked as `draft`
# Note that hugo can opt out of compiling draft posts, but the posts will still exist in the git repo.
PUBLISH_DRAFTS = False

# The Hugo static site generator has some quirks that need to be worked around.
HUGO_HACKS = True


def human_time(seconds_since_epoch):
  return datetime.datetime.fromtimestamp(seconds_since_epoch).astimezone().replace(microsecond=0).isoformat()


class Translator(object):

  def __init__(self, s):
    self.s = s
    self.i = 0
    self.outputs = []
    self.section()

  def next(self, n=1):
    self.i += n
    return self.s[self.i-1]

  def peek(self, a=1, b=0):
    if a > b:
      return self.s[self.i:self.i+a]
    return self.s[self.i+a:self.i+b]

  def has_next(self):
    return self.i < len(self.s)

  def section(self):
    # Starts new output section, erasing the previous section if it was not emitted.
    self.section_start = self.i

  def emit(self):
    # Emit the current section and start a new section.
    self.outputs.append(self.s[self.section_start:self.i])
    self.section()

  def replace(self, repl):
    # Output `repl`` in place of the current section, and start a new section.
    self.outputs.append(repl)
    self.section()

  def __str__(self):
    return ''.join(self.outputs)


class SimpleParser(object):
  RE_LOCAL_LINK = re.compile(r'\[\[(.*?)\]\]', flags=re.DOTALL)
  RE_LOCAL_IMAGE = re.compile(r'!\[\[(.*?)\]\]\n?(\((.*?)\))?', flags=re.DOTALL | re.MULTILINE)
  RE_HIDE_ENDHIDE = re.compile(r'(<!--\s*hide\s*-->.*<!--\s*endhide\s*-->)', flags=re.DOTALL | re.MULTILINE)
  RE_HIDE = re.compile(r'(<!--\s*hide\s*-->.*)', flags=re.DOTALL | re.MULTILINE)
  RE_COMMENT = re.compile(r'(<!--.*?-->)', flags=re.DOTALL | re.MULTILINE)

  def __init__(self):
    self.images = []
    self.pages = []

  def translate(self, s):
    it = Translator(s)

    # Code blocks take precedence over comments, which take precedence over local links and images.

    while it.has_next():
      if it.peek(3) == '```':
        self.code_block(it)
      elif it.peek(1) == '`':
        self.inline_code(it)
      elif it.peek(4) == '<!--':
        it.emit()  # Start new section.
        self.comment(it)
      elif HUGO_HACKS and (it.peek(2) == '$$' and it.peek(-1) != '\\'):
        it.emit()
        self.math_block(it)
      elif HUGO_HACKS and (it.peek(1) == '$' and it.peek(-1) != '\\'):
        it.emit()
        self.inline_math(it)
      elif it.peek(3) == '![[':
        it.emit()
        self.local_image(it)
      elif it.peek(2) == '[[':
        it.emit()
        self.local_link(it)
      else:
        it.next()

    it.emit()  # Emit remaining chars.
    return str(it)

  def inline_code(self, it):
    it.next()  # skip `
    while it.has_next() and it.peek(1) != '`':
      it.next()
    it.next()

  def code_block(self, it):
    it.next(3)  # skip ```
    while it.has_next() and it.peek(3) != '```':
      it.next()
    it.next(3)

  def math_block(self, it):
    it.next(2)  # skip $$
    while not (it.peek(2) == '$$' and it.peek(-1) != '\\'):
      it.next(1)
    it.next(2)
    it.replace(self._math_replace(it.s[it.section_start:it.i]))

  def inline_math(self, it):
    it.next(1)  # skip $
    while not (it.peek(1) == '$' and it.peek(-1) != '\\'):
      it.next(1)
    it.next(1)
    it.replace(self._math_replace(it.s[it.section_start:it.i]))

  def _math_replace(self, s):
    # https://wilsonmar.github.io/markdown-text-for-github-from-html/#special-characters
    return s.replace('\\', '\\\\').replace('*', r'\*').replace('_', r'\_').replace('`', r'\`')

  def comment(self, it):
    # Note, use match rather than search, because it requires that the match be at pos.
    m = self.RE_HIDE_ENDHIDE.match(it.s, it.i)
    if m:
      it.next(len(m.group(0)))
      it.section()
      return

    m = self.RE_HIDE.match(it.s, it.i)
    if m:
      it.next(len(m.group(0)))
      it.section()
      return

    m = self.RE_COMMENT.match(it.s, it.i)
    if m:
      it.next(len(m.group(0)))
      it.section()
      return

    it.next()  # Nothing found. Move forward.

  def local_image(self, it):
    m =self.RE_LOCAL_IMAGE.match(it.s, it.i)
    if m:
      it.next(len(m.group(0)))
      url = f'</{m.group(1)}>'
      if m.group(3):
        # Image caption in group(3)
        it.replace(f'![]({url} "{m.group(3)}")')
      else:
        it.replace(f'![]({url})')
      self.images.append(m.group(1))  # Extract local file name.
      return

    it.next()  # Nothing found. Move forward.

  def local_link(self, it):
    m = self.RE_LOCAL_LINK.match(it.s, it.i)
    if m:
      it.next(len(m.group(0)))
      target = m.group(1)
      if target.startswith('#'):
        # This is a link to a position within this post. Don't treat it like a link to another post.
        it.replace('['+target+']('+target.lower().replace(' ', '-')+')')
      else:
        it.replace('{{< locallink "'+target+'" >}}')
        self.pages.append(target)  # Extract local file name.
      return

    it.next()  # Nothing found. Move forward.


class Context(object):

  def __init__(self, file_name, modify_time, nofail=True):
    self.name = file_name
    self.modify_time = modify_time
    self.nofail = nofail

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    if type is not None:
      # Exception has occurred
      # https://stackoverflow.com/a/18399069
      print(f'Exception in file "{self.name}".')
    return self.nofail  # Reraise exception if false

  def split(self, s):
    if s.startswith('---'):
      i = s.find('---', 3)  # Find closing '---'
      if i >= 0:
        return (yaml.load(s[:i]), s[i+4:])
      else:
        print(s)
        raise Exception('Closing dashes not found in frontmatter')
    else:
      return ({}, s)

  def hugo_frontmatter(self, src_frontmatter):
    # https://www.jvt.me/posts/2019/03/24/datetime-hugo/
    # https://stackoverflow.com/a/28147286
    dest = copy.deepcopy(src_frontmatter)
    del dest['blog']
    if not dest.get('title'):
      # dest['title'] = os.path.splitext(self.name)[0].replace('-', ' ').title()
      dest['title'] = os.path.splitext(self.name)[0]
    dest['date'] = human_time(self.modify_time)
    return dest

  def get_images(self, body):
    return [match[0] for match in re.findall(r'!\[\[(.*?)(\|.*?)?\]\]', body, flags=re.DOTALL | re.MULTILINE)]

  def transform_name(self, name):
    return name  # TODO
    name = src_name.replace(' ', '-').lower()  # Replaces spaces with dashes and convert to lowercase
    name = re.sub(r'[^\w\-.]', '', name)  # Remove symbols
    return name

  def transform_body(self, body):
    # import pdb; pdb.set_trace()
    p = SimpleParser()
    body = p.translate(body)

    return body, p.images

  def q_publish(self, frontmatter):
    # Returns bool indicating whether to copy over to blog.
    return frontmatter and frontmatter.get('blog') is True

  def q_draft(self, frontmatter):
    return frontmatter and frontmatter.get('draft') is True


def cmd(target='.', source='.', clean=False, nofail=False):
  # Get last write time.
  # Get list of changed files.
  # Look at yaml preamble of each file for blog flag (https://yaml.org/spec/1.2/spec.html#id2760395)
  # Copy over transformed markdown to blog repo.

  log_path = os.path.join(source, LOG_FILE)
  cache = {'files': [], 'time': 0}
  if not clean and os.path.isfile(log_path):
    with open(log_path, 'r') as log:
      cache = yaml.load(log.read()) or cache
  if cache['time']:
    print(f'Processing files modified since {human_time(cache["time"])}.')
  else:
    print('Processing all files (clean mode).')
  print('='*32+'\n')

  if clean:
    # https://stackoverflow.com/a/5756937

    # Remove all markdown files in <target>/content/posts/
    files = glob.glob(os.path.join(target, 'content/posts/*.md'))
    for f in files:
      os.remove(f)

    # Remove all files in <target>/static/.
    # This removes images that were copied over.
    files = glob.glob(os.path.join(target, 'static/*'))
    for f in files:
      os.remove(f)

  # Look for files to copy.
  updated_files = []
  for name in os.listdir(source):
    src_full_path = os.path.join(source, name)

    # Only open markdown files.
    if not name.endswith('.md'): continue
    if not os.path.isfile(src_full_path): continue

    # Only open file if it has been modified since the last time this script was run.
    # This will hopefully allow this script to scale to a large number of files, where most have not been touched.
    modify_time = os.path.getmtime(src_full_path)
    if cache['time'] >= modify_time: continue

    # Open file.
    with open(src_full_path, 'r') as stream, Context(name, modify_time, nofail) as c:
      # TODO: If efficiency is an issue, I can read only the first chunk of the file, e.g. `stream.read(1024)`.
      raw = stream.read()
      frontmatter, body = c.split(raw)

      if c.q_publish(frontmatter):  # If this file should be published.
        if c.q_draft(frontmatter) and not PUBLISH_DRAFTS:  # If this file is marked as a draft.
          print(name, '(skipping draft)')
          continue

        updated_files.append(name)
        dest_frontmatter = c.hugo_frontmatter(frontmatter)

        target_name = c.transform_name(name)
        print(name, '-->', target_name)

        # Transform and write markdown.
        dest = os.path.join(target, 'content/posts', target_name)
        with open(dest, 'w') as output:
          # Write frontmatter
          print('---', file=output)
          output.write(yaml.dump(dest_frontmatter, default_flow_style=False))
          print('---', file=output)

          # Write markdown and get referenced image files.
          body, image_files = c.transform_body(body)
          output.write(body)

        # Copy over images embedded in the current file.
        for image_file in image_files:
          print(image_file)
          shutil.copy2(
            os.path.join(source, image_file),
            os.path.join(target, 'static', image_file))  

  # Write out list of all files that have been processed.
  with open(log_path, 'w') as log:
    d = {
        'time': time.time(),
        'files': list(set(cache['files'] + updated_files))}  # dedup
    log.write(yaml.dump(d, default_flow_style=False))


if __name__ == '__main__':
  fire.Fire(cmd)