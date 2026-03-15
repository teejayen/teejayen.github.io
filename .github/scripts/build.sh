#!/bin/bash
set -e

# Generate sitemap lastmod dates from git history
python .github/scripts/update_sitemap_dates.py

# Build Jekyll - include drafts and future posts on non-production branches
if [ "$CF_PAGES_BRANCH" = "main" ]; then
  bundle exec jekyll build
else
  bundle exec jekyll build --drafts --future
fi
