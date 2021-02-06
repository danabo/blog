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


def human_time(seconds_since_epoch):
  return datetime.datetime.fromtimestamp(seconds_since_epoch).astimezone().replace(microsecond=0).isoformat()


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
      dest['title'] = os.path.splitext(self.name)[0].replace('-', ' ').title()
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
    # Remove local-only blocks
    body = re.sub(r'(<!--\s*hide\s*-->.*<!--\s*endhide\s*-->)', '', body, flags=re.DOTALL | re.MULTILINE)

    # Remove everything after unclosed `<!-- hide -->`
    body = re.sub(r'(<!--\s*hide\s*-->.*)', '', body, flags=re.DOTALL | re.MULTILINE)

    # Remove comments
    # https://stackoverflow.com/a/28208465
    body = re.sub('(<!--.*?-->)', '', body, flags=re.DOTALL | re.MULTILINE)

    # Transform internal links (wiki-style links).
    # https://gohugo.io/content-management/cross-references/#use-ref-and-relref
    body = re.sub(r'([^!])\[\[(.*?)\]\]', r'\1{{< locallink "\2" >}}', body, flags=re.DOTALL)

    image_files = self.get_images(body)

    # Transform embedded images '![[...]]' to markdown images
    # ![[image.png]] ==> ![](</image.png>)
    # ![[image.png]]\n(caption) ==> ![](</image.png> "caption")
    # TODO: ![[image.png|size]] ==> ![](</image.png> =size)
    def repl_fun(match):
      url = f'</{match.group(1)}>'
      if match.group(3):
        return f'![]({url} "{match.group(3)}")'
      else:
        return f'![]({url})'
    body = re.sub(r'!\[\[(.*?)\]\]\n?(\((.*?)\))?', repl_fun, body, flags=re.DOTALL | re.MULTILINE)

    return body, image_files

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