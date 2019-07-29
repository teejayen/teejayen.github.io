---
layout: post
title:  "-bash: /bin/rm: Argument list too long"
date:   2019-07-29
---

Just a quick post for future reference...

When using `rm -rf` and receiving errors like `/bin/rm: Argument list too long`, try using `find . -type f -name "*" -exec rm -f {} \;` instead.
