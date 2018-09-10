---
layout: post
title:  "Updating Manager attribute in Office 365 / Azure AD using PowerShell"
date:   2018-09-11
---
Keeping the reporting lines updated in Office 365 is as important as it is tedious, there are a lot of functions which rely on it, such as the Delve Organisation Chart, the "Team" calendar group in Outlook, [SharePoint "Apps"](https://appsource.microsoft.com/en-us/marketplace/apps?search=org%20chart), even Visio has the ability to [automatically generate an organisation chart based on AzureAD](https://support.office.com/en-us/article/create-an-organization-chart-automatically-from-employee-data-8f2e693e-25fc-410e-8264-9084eb0b9360). Using PowerShell with the AzureAD module makes it easy to update user attributes en masse.

First things first, you'll need the [`AzureAD` module](https://docs.microsoft.com/en-gb/powershell/module/AzureAD/?view=azureadps-2.0).  The Azure AD module is distributed using the PowerShell gallery. Installing items from the Gallery requires the latest version of the PowerShellGet module. If you are using Windows 10 or have the Windows Management Framework 5.0 installed, all you need to do is run the following cmdlet:

`Install-Module -Name AzureAD`

Otherwise, you'll need to [Install PowerShellGet](https://docs.microsoft.com/en-us/powershell/gallery/installing-psget).

Unfortunately the AzureAD module hasn't exactly been built with usability in mind, and the majority of the cmdlets both output, and expect the `$ObjectID` as input. There are 168 cmdlets available in the AzureAD module (at time of writing), but I'll just focus on a handful in this post.

In order to get a list of all users use the `Get-AzureADUser` cmdlet, this will return their ObjectID, DisplayName, UserPrincipalName, and UserType.

Of course, the Manager attribute isn't stored as an attribute on the User object - so instead you have to pipe the output to `Get-AzureADUserManager`.

```powershell
Get-AzureADUser | select UserPrincipalName,@{n="Manager";e={(Get-AzureADUser -ObjectId (Get-AzureADUserManager -ObjectId $_.ObjectId).ObjectId).UserPrincipalName}}
```

In order to make changes to all users en masse, you can use something similar to the below:

```powershell
$previousmanager = Get-AzureADUser -Filter "UserPrincipalName eq 'previous@contoso.com'" | Select-Object ObjectID
$newmanager = Get-AzureADUser -Filter "UserPrincipalName eq 'new@contoso.com'" | Select-Object ObjectID

foreach ($user in Get-AzureAdUser) {Get-AzureADUserManager -ObjectID $user.ObjectID | where {$_.ObjectID -eq '$previousmanager'} | Set-AzureADUserManager -RefObjectId "$newmanager"}
```

It's not the most intuitive, but it sure beats clicking through and updating each user manually in GUI!