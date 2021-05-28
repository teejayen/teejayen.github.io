---
layout: post
title:  "OpenVPN connections on macOS Big Sur"
date:   2021-05-28
---
Seemingly, macOS Big Sur does not support NAT based OpenVPN connections - it connects, but you then cannot reach anything on the remote network. The "fix" is to set up a static route, `sudo route -n add 192.168.0.0/22 $utun-ip-address`

Rather than having to do this manually on each computer, you can also have OpenVPN push the route by adding it under `Configuration > Advanced VPN > Private Routed Subnets (Optional)`.