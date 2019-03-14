---
layout: post
title:  "Outlook Direct Connect to Office 365"
date:   2019-03-14
---

I received several panicked calls from one of my clients today - while they are away at a race meet, one by one their Outlook mailbox connections are dropping out and becoming stuck in a never ending loop of prompting for credentials.

Starting in Outlook 2016 version 16.0.6741.2017, Microsoft has included a new feature called Direct Connect to Office 365. It's designed to force Outlook to connect to Office 365 if the user has a mailbox, in order to make it easier for end users to configure Outlook profiles. While it certainly is a neat feature, if you're in the middle of a migration from on-premise Exchange to Office 365 (like they are!) it can cause a great deal of confusion and wasted time trying to troubleshoot the issues.

Fortunately, the fix is quite straight forward but not very well documented. There are two options, a local registry key setting or disabling MAPI on the mailbox in Exchange Online (we opted for the latter to perform the change en masse).

## Registry Key

```
HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\office\16.0\outlook\autodiscover
DWORD: ExcludeExplicitO365Endpoint
Value = 1
```

## Disable MAPI using EXOP

```
Set-CASMailbox -Identity $username -MAPIEnabled $false
```