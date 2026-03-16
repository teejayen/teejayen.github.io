---
layout: post
title: "Azure Files doesn't work with cloud-only Entra-joined devices"
date: 2026-01-07
ai: assisted
---

If you're a cloud-only Microsoft 365 organisation trying to use Azure Files with identity-based authentication, save yourself some time and money: it doesn't work with Entra-joined devices. I spent three days and ~$175/month in Azure resources discovering this.

## The scenario

We wanted to migrate ~2TB of archived project data from on-prem Synology NAS to Azure Files. The appeal: native SMB access, Entra ID integration, no VPN required. Our environment is pure cloud-only - Entra-joined devices with Windows Hello passwordless authentication, no on-prem Active Directory.

## The two options (and why neither works)

### Option 1: Entra Kerberos authentication

Microsoft's documentation makes this sound perfect for cloud-only orgs. The catch buried in the prerequisites: it requires **hybrid identities** - meaning on-prem AD synced via AD Connect. If you're cloud-only, this option is out.

### Option 2: Entra Domain Services

This seemed like the answer. Deploy a managed domain service, enable it on your storage account, done. I deployed Entra DS to `ds.pitchblackgroup.com.au`, configured Tailscale subnet routing for DNS, enabled AADDS authentication on the storage account.

Then came the showstopper: Entra DS requires devices to be **domain-joined** to the managed domain - not just Entra-joined. That means either:
- Deploying GPOs and managing devices like it's 2010
- Running hybrid-join across 100+ remote devices Australia-wide

Both defeat the purpose of being cloud-native.

## The architectural conflict

Here's the fundamental problem Microsoft hasn't solved:

| Auth Method | Requires | Cloud-Only Compatible |
|-------------|----------|----------------------|
| Entra Kerberos | Hybrid identities (on-prem AD + AD Connect) | No |
| Entra Domain Services | Domain-joined devices | No |
| Storage account keys | Nothing | Yes, but no identity |

There's no identity-based Azure Files authentication method for pure cloud-only organisations with Entra-joined devices. It's a genuine product gap.

## What I deployed (and then deleted)

- Entra Domain Services (Standard SKU): ~$165 AUD/month
- Tailscale subnet router VM: ~$10 AUD/month
- Virtual network and associated resources

Total wasted: ~$175/month until I cleaned it up.

## Alternatives

If you're in the same situation, your options are:

1. **Stay on-prem** - Keep your NAS. It works, users know it, and you're not fighting the platform.

2. **Azure Blob with a frontend** - NextCloud/ownCloud with Azure Blob Storage backend. You lose native SMB, but gain Entra SSO via SAML/OAuth.

3. **SharePoint/OneDrive** - If your use case fits the sync model and file size limits.

4. **Wait** - Microsoft may eventually ship a solution. There's a preview for "cloud-only Entra Kerberos" but it's not GA and has its own limitations.

## The lesson

Microsoft's documentation doesn't clearly state the incompatibility between Azure Files identity auth and cloud-only Entra-joined devices. You have to piece it together from prerequisites scattered across multiple pages.

Before deploying Azure infrastructure, verify the authentication chain end-to-end - not just whether the service supports Entra, but whether your specific device and identity configuration is supported.

## References

- [Azure Files identity-based authentication](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-auth-domain-services-enable)
- [Entra Kerberos prerequisites](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable) (note the hybrid identity requirement)
