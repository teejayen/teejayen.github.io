---
layout: post
title:  "Securing Mikrotik RouterOS"
date:   2018-10-07
---
Several Mikrotik routers we manage were recently exploited with a Winbox vulnerability ([CVE-2018-14847](https://nvd.nist.gov/vuln/detail/CVE-2018-14847), more information available [here](https://forum.mikrotik.com/viewtopic.php?t=133533)) and used to send email spam. Even though it was supposedly fixed with RouterOS 6.41.21, even after upgrading to 6.43.23 we encountered some devices that were still sending spam emails. It was only after locking down any unrequired services (specifically the SOCKS proxy) that it stopped.

This served as a reminder to ensure standard configuration, especially when it comes to security. Below is a snippet of the configuration we have rolled out:

First things first, change the default username and password.

```
/user set 0 password=correcthorsebatterystaple
/user set 0 name=routerosadmin comment="Default account, do not use for normal access!"
```

Create individual user accounts for all users who will need to administer the devices.

```
/user add name=tim password=correcthorsebatterystaple group=full comment="Timothy Neilen - answers IT"
```

Disable all unrequired services, especially when they aren't encrypted... and when they are encrypted lock them down to only be accessible from certain IPs!

```
/ip service disable [find name=telnet]
/ip service disable [find name=ftp]
/ip service disable [find name=www]
/ip service disable [find name=www-ssl]
/ip service disable [find name=api]
/ip service disable [find name=api-ssl]
/tool bandwidth-server set enabled=no
/ip dns set allow-remote-requests=no
/ip socks set enabled=no
/ip service set winbox address=10.0.0.0/24,115.70.222.205/32
/ip service set ssh address=10.0.0.0/24,115.70.222.205/32
```

As a throwback to IOS days we set a MOTD too - it probably won't deter any would be attackers, and it certainly won't stop automated bruteforce attacks but if someone does gain access it's a reminder that they are being monitored!

```
/system note set show-at-login=yes
/system note set note="You must have explicit, authorized permission to access or configure this device. Unauthorised attempts and actions to access or use this system may result in civil and/or criminal penalties. All activities performed on this device are logged and monitored."
```