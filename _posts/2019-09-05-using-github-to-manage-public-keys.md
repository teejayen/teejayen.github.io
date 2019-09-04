---
layout: post
title:  "Using GitHub to manage public keys"
date:   2019-09-05
---

Authentication with remote services is often accomplished with SSH Keys. While being a very secure, it can be a bit tedious to set up and manage. The best way I've found to manage my public keys is to simply add them to GitHub ([instructions available here](https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account)). From there it's a matter of sending through a [link to the public keys](https://github.com/teejayen.keys) if I ever need to be granted remote access.

By adding the keys to GitHub, you can also use `curl` to add them to authorized_keys:

`curl https://github.com/your-username.keys >> ~/.ssh/authorized_keys`

