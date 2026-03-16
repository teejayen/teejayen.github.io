---
layout: post
title: "Tailscale grants bypass Starter plan ACL limitations"
date: 2026-01-07
ai: assisted
---

Tailscale's Starter plan has a significant ACL limitation that isn't immediately obvious: you can only use `autogroup:admin` and `autogroup:member` in your ACL rules. Custom groups, individual users, and tags are all blocked.

Except they're not - if you use grants instead of ACLs.

## The limitation

On Starter plan, this ACL rule fails validation:

```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["group:it-admins"],
      "dst": ["tag:server:*"]
    }
  ]
}
```

Error: Custom groups not available on Starter plan.

The only sources you can use are `autogroup:admin` (tailnet admins) and `autogroup:member` (everyone). Fine-grained network segmentation seems impossible.

## The workaround: Grants

Grants are Tailscale's newer, more flexible permission model. And crucially, they don't have the same Starter plan restrictions.

This works:

```json
{
  "grants": [
    {
      "src": ["group:it-admins"],
      "dst": ["tag:server"],
      "ip": ["*"]
    }
  ]
}
```

You can use:
- Custom groups (defined in the same policy file)
- Individual users by email
- Tags
- Specific ports and protocols

## Policy structure

Here's the pattern I use:

```json
{
  "groups": {
    "group:it-admins": ["tim@company.com", "hudson@company.com"],
    "group:engineers": ["autogroup:member"]
  },

  "tagOwners": {
    "tag:server": ["group:it-admins"],
    "tag:workstation": ["autogroup:admin"]
  },

  "hosts": {
    "proxmox-01": "10.157.1.10",
    "n8n": "10.157.1.20"
  },

  "grants": [
    {
      "src": ["group:it-admins"],
      "dst": ["tag:server"],
      "ip": ["*"]
    },
    {
      "src": ["group:engineers"],
      "dst": ["n8n"],
      "ip": ["443/tcp"]
    },
    {
      "src": ["autogroup:member"],
      "dst": ["autogroup:member"],
      "ip": ["*"]
    }
  ]
}
```

The last grant is the "allow all" fallback - keep this while you're testing, then remove it once your specific grants are validated.

## Migration approach

1. **Discover** - Export your current device list, identify what needs segmentation
2. **Tag** - Apply tags to devices (servers, workstations, subnet routers)
3. **Define grants** - Start permissive, use host aliases for clarity
4. **Test** - Uncomment specific grants, verify access works
5. **Tighten** - Remove the allow-all grant once confident

## What grants can't do

Network segmentation only works for direct connections. If you're running services behind a reverse proxy (Nginx Proxy Manager, Traefik), all traffic comes from the proxy's IP. You can't segment access to individual services on the same host - use application-level authentication instead.

## Device limits

Starter plan allows 100 devices. We're at 111 and still working (grandfathered?), but worth monitoring if you're growing. Premium unlocks unlimited devices plus proper SCIM/Entra group sync.

## References

- [Tailscale Grants](https://tailscale.com/kb/1324/grants)
- [Grants vs ACLs](https://tailscale.com/kb/1467/grants-vs-acls)
- [ACL syntax](https://tailscale.com/kb/1337/acl-syntax)
