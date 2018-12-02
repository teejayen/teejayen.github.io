---
layout: post
title:  "Windows 7 Update Reboot Loop"
date:   2018-11-21
---

We have had a couple of customers report restart loop issues, despite multiple restarts it still prompts them to restart again.. and again. I've not been able to determine which specific update is causing it, but the fix is as simple as removing the RebootRequired registry key.

I've scripted this to run across all Windows 7 computers, which has saved as a lot of unnecessary phone calls.

`reg delete HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired /v CleanShutdown /f`