---
layout: post
title:  "Displaying terminal colours"
date:   2019-08-02
---

I'm in the middle of shifting from ConEmu to Windows Terminal, and have been playing around with colour schemes - so was trying to find an easy way to output all colours in the terminal, the snippets below helped.

## PowerShell

```powershell
[enum]::GetValues([System.ConsoleColor]) | Foreach-Object {Write-Host $_ -ForegroundColor $_}
```

## Bash

```bash
for x in {0..8}; do for i in {30..37}; do for a in {40..47}; do echo -ne "\e[$x;$i;$a""m\\\e[$x;$i;$a""m\e[0;37;40m "; done; echo; done; done; echo ""
```

## Command Prompt

First, install [ColorTool](https://github.com/Microsoft/Terminal/tree/master/src/tools/ColorTool) and then use:

```cmd
colortool -c
```