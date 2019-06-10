---
layout: post
title:  "RDP, UDP, VPN"
date:   2019-06-10
---
We've been moving our clients to using VPN connections (SSL VPN using WatchGuards, specifically) when they need to access their computers via RDP, and don't have a Remote Desktop Server in place. Not only is opening up port 3389 a major attack vector with no bruteforce protection, but new vulnerabilties such as BlueKeep and BlackSquid don't even need to authenticate to exploit the RDP protocol.

There have been a couple of instances where clients have reported drop outs and freezing, it only happens for a couple of seconds but is quite an annoyance.

Turns out by default, RDP will try to use UDP for connections to provide a better user experience on slow connections - but with the VPN in the mix, it causes a lot of fragmentation which can't be properly reassembled. This leads to the drop outs, black screens and freezings.

The work around which we have used with success is to disable the UDP protocol in Remote Desktop. This can be done through the Registry, or Group Policy:

## Registry

1. Navigate to `HKLM\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services\Client`.

2. Create a DWORD named **fClientDisableUDP** and assign it a value of **1**.

## Group Policy

1. Navigate to Computer Configuration > Administration Templates > Windows Components > Remote Desktop Services > Remote Desktop Connection Client.

2. Set **Turn Off UDP On Client** to Enabled.