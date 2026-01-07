---
layout: post
title: "Microsoft Authenticator keeps dropping off on Android"
date: 2026-01-07
ai: assisted
---

If you're managing Microsoft 365 and have users whose Microsoft Authenticator app keeps "dropping off" their Android phones, here's what's likely happening and how to fix it.

## The symptom

User sets up Authenticator, it works for a while, then stops. You re-register it, works again, then stops. Rinse and repeat. The app logs are useless - just experimentation flags and feature toggles.

## The cause

When Android performs a major version update, it can invalidate the cryptographic keys used for device attestation. The problem is that Entra ID creates a *new* device registration for the updated OS, but the Authenticator method remains bound to the *old* device registration.

You end up with duplicate device entries in Entra for the same physical phone - one stale, one current. The Authenticator app gets confused about which device identity to use.

## How to diagnose

Query Entra via Graph API or the admin centre:

1. Check the user's registered devices - look for duplicates of the same phone model with different OS versions
2. Check when their Authenticator method was created vs when the newer device registration appeared
3. Look at sign-in logs for errors `50129` ("device is not workplace joined") or `50097` ("device authentication required")

Here's a quick PowerShell snippet to check:

```powershell
Connect-MgGraph -Scopes 'User.Read.All','UserAuthenticationMethod.Read.All'

$user = Get-MgUser -Filter "mail eq 'user@domain.com'"

# Check for duplicate device registrations
Get-MgUserRegisteredDevice -UserId $user.Id |
    Select-Object @{N='Name';E={$_.AdditionalProperties.displayName}},
                  @{N='OS';E={$_.AdditionalProperties.operatingSystemVersion}},
                  @{N='Created';E={$_.AdditionalProperties.createdDateTime}}

# Check Authenticator method creation date
Get-MgUserAuthenticationMicrosoftAuthenticatorMethod -UserId $user.Id |
    Select-Object DisplayName, DeviceTag, PhoneAppVersion, CreatedDateTime
```

## The fix

1. Delete the stale device registration (the old OS version) from Entra ID > Devices
2. Delete the Authenticator authentication method from the user's account
3. Have the user remove the work account from Authenticator on their phone
4. Issue a TAP and re-register fresh

The key insight is that deleting the authentication method alone isn't enough - you need to clean up the orphaned device registration too, or the same binding issue will recur.

## Conditional Access consideration

If you're using `deviceBasedPush` in your authentication strength policies (common in passwordless configurations), this issue will hit harder because valid device binding is required. Users with standard push notifications may not notice until the stale registration causes other problems.
