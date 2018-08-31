---
layout: post
title:  "Adding Distribution Group Members to a Dynamic Distribution Group"
date:   2018-08-06
---
As a follow up to the previous post, [Dynamic Distributions Groups based on Organisational Units](/2018/05/26/dynamic-distribution-groups-based-on-organisational-units), the client wanted to add their Executive Leadership Team (some based in NZ, others based in AU) to both country wide Dynamic Distribution Groups. 

After a bit of Googling and testing, it turns out you can add a filter to the Dynamic Distribution Group based on matching the *alias* of the regular Distribution Group to achieve the desired outcome.

```powershell
    Set-DynamicDistributionGroup -Name "AU Staff" -IncludedRecipients "MailboxUsers" -RecipientFilter ((CustomAttribute12 -eq 'Australia') -and (-not(CustomAttribute11 -eq 'Meeting Rooms') -or (Alias -eq 'executiveleadershipteam')))

    Set-DynamicDistributionGroup -Name "NZ Staff" -IncludedRecipients "MailboxUsers" -RecipientFilter ((CustomAttribute12 -eq 'New Zealand') -and (-not(CustomAttribute11 -eq 'Meeting Rooms') -or (Alias -eq 'executiveleadershipteam')))

    Set-DynamicDistributionGroup -Name "PH Staff" -IncludedRecipients "MailboxUsers" -RecipientFilter ((CustomAttribute12 -eq 'Philippines') -and (-not(CustomAttribute11 -eq 'Meeting Rooms') -or (Alias -eq 'executiveleadershipteam')))
```