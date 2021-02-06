#!/bin/sh
# https://gohugo.io/hosting-and-deployment/hosting-on-github/#put-it-into-a-script-1

# Set BLOG_SOURCE environment variable.

# https://stackoverflow.com/a/21128172
f_flag='false'
clean='false'
while getopts 'fc' flag; do
  case "${flag}" in
    f) f_flag='true' ;; # force
    c) clean='true'  ;; # clean
  esac
done

if [ "`git status -s`" ]
then
    if [ "$f_flag" == "true" ]
    then
        echo "WARNING: The working directory is dirty."
    else
        echo "FATAL: The working directory is dirty. Please commit any pending changes."
        exit 1;
    fi
fi

# Running blog.py
./blog.py --source=$BLOG_SOURCE --clean=$clean
echo "\nFiles processed"

# Confirm changes
git add -A
git commit -v || { echo 'Exiting' ; exit 1; } # Ask user to confirm diff before committing
git push  # Push to master branch

# Push to gh-pages branch
echo "Deleting old publication"
rm -rf public
mkdir public
git worktree prune
rm -rf .git/worktrees/public/

echo "Checking out gh-pages branch into public"
git worktree add public gh-pages

echo "Removing existing files"
rm -rf public/*

echo "Generating site"
hugo

echo "Updating gh-pages branch"
cd public \
    && git add --all \
    && git commit -m "Publishing to gh-pages" \
    && echo "Pushing to github" \
    && git push --all \
    && cd ..
