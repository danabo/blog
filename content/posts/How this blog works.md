---
date: '2021-02-07T21:01:53-06:00'
tags:
- personal
- blogging
title: How this blog works
---

This blog is a window into my second brain. That is where I store all of my personal notes, ranging from journal entries to productive materials like study notes and math problems. I can mark any of these items for publication on my blog, and I have a script take care of the rest.

# Second brain
I use the [Obsidian](https://obsidian.md/) editor to organize my second brain. It looks like this:

![](</Pasted image 20210206135929.png> "Writing some blog posts in Obsidian.")

Every note is a markdown file, with support for extra features like [MathJax](https://www.mathjax.org/) (latex math mode), and some of the features in [Roam](https://roamresearch.com/), namely [wiki-style internal links](https://publish.obsidian.md/help/How+to/Format+your+notes). So `[[Blogging experiment]]` becomes {{< locallink "Blogging experiment" >}}. It has some convenient features like being able to paste images from my clipboard and auto-generate an image embed command: 

![](</Pasted image 20210206140636.png> "Previous screenshot I pasted into this very markdown file.")

There is also a nifty graph view of all my notes:

![](</Pasted image 20210206140906.png> "Looks like a constellation! Each node is a markdown file. Each edge is due to one file linking to another with `[[...]]`. I'm not yet sure how helpful this is, but it's nice to have a way to look at everything at once, in lieu of a traditional hierarchical structure.")

# Publishing flow
My blog is written in [Hugo](https://gohugo.io/) (for now), which is a static site generator that takes markdown files as input. Ideally, I could just run hugo directly on my Obsidian directory, but (1) I don't want to publish everything and (2) Obsidian defines its own extended markdown syntax, as I explained above. My workaround is to have a script copy and transform my Obsidian notes marked for publication. Here's how I do it...

Markdown files can optionally have a frontmatter, which is a yaml header at the top of the page. For example:

```yaml
---
title: Hello World
author: John Doe
---
```

In any note in my second brain (Obsidian), I can set `blog: true` and that note will be published on my blog.

Every so often, I run [publish.sh](https://github.com/danabo/blog/blob/master/publish.sh) from the blog repo, which in turn runs [blog.py](https://github.com/danabo/blog/blob/master/blog.py).

[blog.py](https://github.com/danabo/blog/blob/master/blog.py) is where the magic happens. It's a Python script that uses [fire](https://github.com/google/python-fire) to give it a [CLI](https://en.wikipedia.org/wiki/Command-line_interface). It will go through all the markdown files in my second brain directory and look for the ones with frontmatter containing `blog: true`. For those files, it will do a few transformations, like converting internal links, `[[...]]` and Obsidian's image command `![[...]]` to regular markdown. It also scrubs markdown comments, `<!-- ... -->`, and anything inside a `<!-- hide -->...<!-- endhide -->` pair so that I can have private sections inside published notes.

Code to transform Obsidian markdown to [Hugo](https://gohugo.io/) markdown:
```python
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
    body = re.sub(r'([^!])\[\[(.*?)\]\]', r'\1\{\{\< locallink "\2" \>\}\}', body, flags=re.DOTALL)
```

[*Edit: I've since updated [blog.py](https://github.com/danabo/blog/blob/master/blog.py) to use an iterator-based parser so that I can ignore comments and wiki-links inside code blocks, which is a problem I ran into writing this very post!*]

For internal links, I call the [locallink](https://github.com/danabo/blog/blob/master/layouts/shortcodes/locallink.html) Hugo [shortcode](https://gohugo.io/content-management/shortcodes/) I made, i.e. `{{ locallink "..." }}`, which checks if the given post name exists. If so, it returns an anchor to the absolute URL for that note. If not, it returns a *red* anchor indicating the post does not exist, {{< locallink "like this" >}}. That way, if I've referenced a note that is not marked for publication, the current note will be published. The red link is kind of like a [missing wiki page](https://en.wikipedia.org/wiki/Wikipedia:Red_link). Perhaps if readers become curious about notes I didn't publish, I might become motivated to publish them.

locallink [Hugo](https://gohugo.io/) shortcode:
```html
{{ $name := (.Get 0) }}
{{ $postFile := (print "content/posts/" $name ".md") }}
{{ if (fileExists $postFile) }}
<a href\="{{ ref . $name }}"\>{{ $name }}</a\>
{{ else }}
<a href\="" class\="broken"\>{{ $name }}</a\>
{{ end }}
```

[publish.sh](https://github.com/danabo/blog/blob/master/publish.sh) will first run blog.py, and then run `git commit -v` which shows me the diff. If I add a commit description in the prompt, publish.sh will go ahead and push the changes, and then update the gh-pages branch. If I quit the editor without adding a commit message, publish.sh will abort.
