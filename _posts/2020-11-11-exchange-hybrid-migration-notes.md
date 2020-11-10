---
layout: post
title:  "Exchange Hybrid Migration notes and snippets"
date:   2020-11-11
---

*Just putting my rough notes / PowerShell snippets I've found handy during an Exchange 2010 -> Exchange Online hybrid migration in one place.Will tidy up soon!*

## Get status of all mailbox move requests from a single batch
```powershell
Get-MigrationUser -BatchId "Batch 3" | Get-MigrationUserStatistics | Select-Object Identity,Status,EstimatedTotalTransferSize,BytesTransferred
```

## Get status of all mailbox move requests

```powershell
Get-MoveRequest | Get-MoveRequestStatistics | Select-Object Identity,Status,TotalMailboxSize,BytesTransferred
```


## Complete individual mailbox move request from a batch

```powershell
Set-MoveRequest $mailbox -SkippedItemApprovalTime  $(Get-Date).ToUniversalTime()
Set-MoveRequest $mailbox -CompleteAfter 1
```


## Remove existing ADAL identities if Outlook doesn't prompt

```powershell
Get-ChildItem -Path "HKCU:\Software\Microsoft\Office\16.0\Common\Identity\Identities" | Remove-Item
cmdkey /list | ForEach-Object{​​​​​​​​​if($_ -like "*Target:*"){​​​​​​​​​cmdkey /del:($_ -replace " ","" -replace "Target:","")}​​​​​​​​​}​​​​​​​​​
```


## Install Azure AD Directory Broker Plugin

```powershell
if (-not (Get-AppxPackage Microsoft.AAD.BrokerPlugin)) { Add-AppxPackage -Register "$env:windir\SystemApps\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy\Appxmanifest.xml" -DisableDevelopmentMode -ForceApplicationShutdown } Get-AppxPackage Microsoft.AAD.BrokerPlugin
```

Found [here](https://www.kiloroot.com/modern-authentication-issues-with-office-365-fixed-dont-just-disable-azure-active-directory-authentication-library-adal-instead-fix-it-with-this/).