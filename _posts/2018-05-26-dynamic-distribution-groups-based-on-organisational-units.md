---
layout: post
title:  "Dynamic Distributions Groups based on Organisational Units"
date:   2018-05-26 13:33:00 +1000

---
One of my clients from [answers IT](https://answersit.com.au) requested that existing Distribution Groups for "all staff" at each site were reviewed recently, as a significant amount of terminated staff were still in the list. For this client, generally the user termination process is to disable the Active Directory user account, move it to the "Disabled" Organisational Unit (OU) convert the user mailbox to a shared mailbox and then hide it from the Global Address List (GAL). As they have had quite a few employees who have left and then returned, their account can be easily re-enabled for use.

Rather than painstakingly reviewing disabled user accounts, documenting their group membership and then removing them, I thought why not investigate Dynamic Distribution Groups. Members of Dynamic Distribution Groups are determined each time a message is sent to the group, based on filters and conditions specified. However, Office 365 only provides a handful of filters through the GUI so it's best to jump in to Exchange Online via PowerShell to set these up.

Out of the box Microsoft Azure Active Directory Connect (AAD Connect) synchronises [quite a few attributes](https://docs.microsoft.com/en-us/azure/active-directory/connect/active-directory-aadconnectsync-attributes-synchronized) to Office 365. However Distinguished Name (DN) or OU (which technically isn't a user attribute) are not included by default. So, to synchronise these as attributes a new inbound synchronisation rule which uses transformations was set up:

From the server which runs AAD Connect:

1. Start the Synchronization Rules Editor by going to Start > Synchronization Rules Editor.
2. Set the search filter Direction to be Inbound.
3. Select Add new rule.
4. On the Description page, set the following configuration:
    ![Description](/assets/images/dynamic-distribution-groups-based-on-organisational-units/description.png)
5. Leave both Scoping filter and Join rules blank.
6. Transformation rules is where the magic happens, for this specific use case we synchronised the DN, and a couple of different OUs (due to the nested organisation we use):
    ![Transformation rules](/assets/images/dynamic-distribution-groups-based-on-organisational-units/transformationrules.png)
7. Perform an initial sync, which will resynchronise all attributes:
    ```powershell
    Start-ADSyncSyncCycle -PolicyType Initial
    ```

A list of all available functions that can be used with AAD Connect is available from [Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/connect/active-directory-aadconnectsync-functions-reference).

Now onto setting up the Dynamic Distribution Groups, for the client this included Country Wide groups and then also groups for their head offices in Australia and New Zealand:

1. [Connect to Office 365 via PowerShell](https://github.com/teejayen/powershell.snippets/blob/master/Connect-O365Session.ps1).
2. Create the new Dynamic Distribution Groups:
    ```powershell
    New-DynamicDistributionGroup -Name "AU Staff" -IncludedRecipients "MailboxUsers" -RecipientFilter ((CustomAttribute12 -eq 'Australia') -and (-not(CustomAttribute11 -eq 'Meeting Rooms'))

    New-DynamicDistributionGroup -Name "NZ Staff" -IncludedRecipients "MailboxUsers" -RecipientFilter ((CustomAttribute12 -eq 'New Zealand') -and (-not(CustomAttribute11 -eq 'Meeting Rooms'))

    New-DynamicDistributionGroup -Name "PH Staff" -IncludedRecipients "MailboxUsers" -RecipientFilter ((CustomAttribute12 -eq 'Philippines') -and (-not(CustomAttribute11 -eq 'Meeting Rooms'))

    New-DynamicDistributionGroup -Name "Onehunga Staff" (((CustomAttribute12 -eq 'New Zealand') -and (City -eq 'Onehunga'))) -and (-not(CustomAttribute11 -eq 'Meeting Rooms'))

    New-DynamicDistributionGroup -Name "Eight Mile Plains Staff" (((CustomAttribute12 -eq 'Australia') -and (City -eq 'Eight Mile PLains'))) -and (-not(CustomAttribute11 -eq 'Meeting Rooms'))
    ```

By filtering based on the CustomAttributes (which are synchronised from Active Directory OU) this ensures that only active user accounts will be in the group, and in the case of some Filipino staff who may have their address attributes set to AU/NZ it ensures they won't receive emails destined for users who are physically based out of these offices.

It was then a simple process of removing the Primary SMTP Address from the old Distribution Groups, adding it to the new Dynamic Distribution Groups and hiding the previous Distribution Groups from the GAL - as unfortunately it wasn't known whether these groups were used for setting permissions to mailboxes, SharePoint, PowerBI, etc. So, the next post will likely cover how to check whether Distribution Groups have been used to set permissions.