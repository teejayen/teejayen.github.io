---
layout: post
title:  "Unifi Controller install woes - Cannot locate Java Home"
date:   2019-03-15
---

answers IT are currently on a WatchGuard roll out spree for our clients, and with that comes lots of old hardware - so I decided to salvage a few Ubiquiti devices which had been replaced to test out and find the limits of at home.

I have a [Vultr 512MB VPS](https://www.vultr.com/?ref=7139744) that is infrequently used (it runs a couple of low traffic WordPress sites). so I opted to run the Unifi Controller on it. Following through the [Unifi Controller installation steps](https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-and-Update-via-APT-on-Debian-or-Ubuntu4) was straight forward, and the sheer amount of updates reminded me just how long ago it was since I had logged in (mid 2017!). Everything seemed to install fine, but when trying to reach the controller via the web interface it simply wouldn't respond.

`system start unifi` didn't give any errors. `sudo lsof -i -P -n | grep LISTEN` didn't return any the normal open ports however. `systemctl status unifi` revealed the issue:

```
Mar 15 10:38:24 tjn-wp-lv01 systemd[1]: Starting unifi...
Mar 15 10:38:24 tjn-wp-lv01 unifi.init[29904]:  * Starting Ubiquiti UniFi Controller unifi
Mar 15 10:38:24 tjn-wp-lv01 unifi.init[29904]: Cannot locate Java Home
```

A Google search lead me to a [post on the Ubiquiti forums](https://community.ubnt.com/t5/UniFi-Wireless/Java-Home-Directory-Fail-Issue-on-Ubuntu-RESOLVED/td-p/474037) to set the `JAVA_HOME` variable in /etc/init.d/unifi to `$( readlink -f "$( which java )" | sed "s:bin/.*$::" )"`, still no luck.

`whereis java` revealed that Java was indeed installed, and `java -version` confirm that openjdk version "9-internal" was in use. Another Google search lead me to yet [another post on the Ubiquiti forums](https://community.ubnt.com/t5/UniFi-Wireless/Running-Unifi-Controller-on-Java-9-10-and-11/td-p/2532928) which pointed out that the Unifi Controller requires the activation.jar from the JavaBeans Activation Framework - it used to be included in Java SE, but is deprecated in Java 9 and 10, and removed in Java 11.

The path forward was now clear, install Java 8 which includes the JavaBeans Activation Framework - a handful of commands later and the Unifi Controller was up and running, ready to adopt devices:

```bash
add-apt-repository ppa:webupd8team/java
apt-get update
apt-get install oracle-java8-installer
apt-get install oracle-java8-set-default
echo JAVA_HOME="/usr/lib/jvm/java-8-oracle" >> /etc/environment
source /etc/environment
systemctl start unifi
```

Next time I will probably just use Docker...