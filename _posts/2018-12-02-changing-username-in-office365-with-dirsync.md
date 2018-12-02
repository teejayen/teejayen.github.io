---
layout: post
title:  "Changing username in Office 365 that is directory synchronised"
date:   2018-12-02
---
When using Azure AD Connect, the userPrincipalName attribute in Active Directory is used to set the user name in Office 365. This username is used for all Office 365 services such as Outlook Web Access, ActiveSync, SharePoint, etc.

It's not possible to change the username in Office 365 admin console and you will receive a message, "This user is synchronized with your local Active Directory. Some details can be edited only through your local Active Directory."

![Edit username](/assets/images/changing-user-name-in-office365-that-is-directory-synchronised/editusername.png)

When changing the userPrincipalName attribute in Active Directory it still won't synchronise the change to Office 365, even when using the `-PolicyType Initial` flag. The only way to update the username / User Principal Name in Office 365 is to use the [Microsoft Azure Active Directory Module for Windows PowerShell](https://www.powershellgallery.com/packages/MSOnline/1.1.183.17) with the the following command:

`Set-MsolUserPrincipalName -UserPrincipalName finance@contoso.onmicrosoft.com -NewUserPrincipalName finance@contoso.com`