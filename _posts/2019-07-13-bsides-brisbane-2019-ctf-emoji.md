---
layout: post
title:  "BSides Brisbane 2019 CTF - emoji"
date:   2019-07-13
---

**Category:** misc

**Points:** 200

**Solves:** 4

**Description:** There's always one of these, isn't there? flag is of the format flag{text}. _Plus a download in the form of emoji.txt._

**emoji.txt contents:**
```
😀😀😀😀😀😀😀😀😀😀[🙃>😀😀😀😀😀😀😀😀😀😀<]>😀😀.😀😀😀😀😀😀.<😀😀😀[🙃>🙃🙃🙃<]>🙃🙃.😀😀😀😀😀😀.<
😀😀😀😀[🙃>😀😀😀😀<]>😀😀😀😀.<😀😀😀😀😀😀[🙃>🙃🙃🙃🙃🙃🙃<]>🙃🙃🙃.<😀😀😀😀[🙃>😀😀😀😀<]>😀😀😀
😀.<😀😀😀😀😀😀😀[🙃>🙃🙃🙃🙃🙃🙃🙃<]>🙃🙃🙃🙃🙃🙃.<😀😀😀😀😀😀😀😀[🙃>😀😀😀😀😀😀😀😀<]>😀😀.<😀😀😀
😀[🙃>🙃🙃🙃🙃<]>🙃🙃🙃🙃.<😀😀😀[🙃>😀😀😀<]>😀.<😀😀😀[🙃>😀😀😀<]>😀.<😀😀😀😀[🙃>🙃🙃🙃🙃<]
>🙃🙃🙃🙃.<😀😀😀😀[🙃>😀😀😀😀<]>😀😀😀😀😀.<😀😀😀😀😀😀[🙃>🙃🙃🙃🙃🙃🙃<]>🙃🙃🙃🙃🙃🙃🙃🙃.<😀😀😀😀
[🙃>🙃🙃🙃🙃<]>🙃🙃🙃🙃🙃.<😀😀😀😀😀😀[🙃>😀😀😀😀😀😀<]>😀😀😀😀😀😀😀😀.<😀😀😀😀[🙃>😀😀😀😀<]>😀
😀😀😀.<😀😀😀😀😀😀😀😀[🙃>🙃🙃🙃🙃🙃🙃🙃🙃<]>🙃🙃🙃.<😀😀😀😀😀😀😀[🙃>😀😀😀😀😀😀😀<]>😀😀😀😀😀😀😀😀
😀😀😀😀😀.🙃🙃🙃🙃🙃🙃🙃.🙃🙃🙃🙃🙃🙃🙃🙃.<😀😀😀😀[🙃>😀😀😀😀<]>😀😀😀😀😀.<😀😀😀[🙃>🙃🙃🙃<]>🙃🙃🙃
.<😀😀😀😀😀😀😀[🙃>🙃🙃🙃🙃🙃🙃🙃<]>🙃🙃🙃.<😀😀😀😀😀😀😀😀[🙃>😀😀😀😀😀😀😀😀<]>.<😀😀😀😀[🙃>🙃🙃
🙃🙃<]>🙃🙃🙃🙃🙃.😀😀😀😀😀.<😀😀😀😀😀😀😀[🙃>🙃🙃🙃🙃🙃🙃🙃<]>🙃🙃🙃.<😀😀😀😀😀😀😀😀[🙃>😀😀😀😀😀😀
😀😀<]>😀😀😀😀😀😀😀😀😀😀.<😀😀😀😀[🙃>🙃🙃🙃🙃<]>🙃🙃🙃🙃🙃.😀😀😀😀😀😀😀😀😀.<😀😀😀[🙃>🙃🙃🙃<]>
🙃🙃🙃🙃🙃🙃.<😀😀😀😀[🙃>😀😀😀😀<]>😀😀😀😀😀.<😀😀😀[🙃>🙃🙃🙃<]>🙃🙃🙃🙃🙃🙃.😀😀😀😀😀😀😀😀😀.<😀
😀😀[🙃>🙃🙃🙃<]>🙃.<😀😀😀😀😀[🙃>😀😀😀😀😀<]>.<
```

Though some may recognise it, googling programming languages should reveal the syntax belongs to the esoteric programming language ["Brainfuck"](https://en.wikipedia.org/wiki/Brainfuck), however, `+` has been substituted with `😀`, and `-` substituted with `🙃`. Change these back using whatever tool you want (find + replace in VSCode was enough for me). Running this through an interpreter, such as [copy.sh/brainfuck/](https://copy.sh/brainfuck/) reveals the flag: `flag{Th1s_is_tH3_s0ng_th4t_d0zen_tend}`

I didn't solve **emoji** on the day, but went back to have a look after solving Brainy's Cipher on HTB and got the flag.
