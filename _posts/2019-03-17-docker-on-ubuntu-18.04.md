---
layout: post
title:  "Docker on Ubuntu 18.04"
date:   2019-03-17
---

I've been using a [Gigabyte BRIX](https://www.gigabyte.com/au/Mini-PcBarebone) as a pseudo home lab machine running ESXi for a while now, but I thought it was time to give containers a try - being fairly familiar with Ubuntu / Debian I decided to download the latest version, 18.04 LTS, to use Docker on Ubuntu. Conveniently enough, during the install process Ubuntu asks if you want to install some popular packages and it was no surprise that Docker was presented as a option.

These packages are based on their new Snapcraft framework which runs applications in a container, so running Docker in a Snap is essentially running a container in a container.

![YO DAWG!](/assets/images/docker-on-ubuntu-18/yodawg.jpg)

Initially everything seemed to be working swimmingly, no issues with build / push / pull commands - but when trying to use `docker-compose` after cloning a [git repository for ELK](https://github.com/deviantony/docker-elk) it started getting screwy:

```
sudo docker-compose up -d
ERROR:
        Can't find a suitable configuration file in this directory or any
        parent. Are you in the right directory?

        Supported filenames: docker-compose.yml, docker-compose.yaml
```

After triple checking that docker-compose.yml did indeed exist, pulling my hair out, and a lot of Google-ing it turns out Snap packages run in an [AppArmor sandbox](https://wiki.ubuntu.com/AppArmor) which will set up a private /tmp using a per-snap private mount namespace and mounting a per-snap directory on /tmp, rather than using the host /tmp directory. ``docker-composer`` writes files to the /tmp directory and ignores the TMPDIR environment variables, and for whatever reason it just wouldn't work. While I could of spent a substantial amount of time trying to get it all working, I decided to remove the snap (`sudo snap remove docker`), and then [install Docker using the official method](https://docs.docker.com/install/linux/docker-ce/ubuntu/) - everything in home lab land was in harmony again!

As a side note, the [Docker Snap](https://github.com/docker/docker-snap) has been deprecated and is no longer being maintained by Docker. There is some [limited discussion about it on the Snapcraft forums](https://forum.snapcraft.io/t/the-future-of-the-docker-snap/7218/23), but no clear reason exactly why it was deprecated in the first place.