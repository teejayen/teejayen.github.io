---
layout: post
title:  "Where's our data gone‽, or Disappearing EBS volumes"
date:   2018-06-21 00:23:00 +1000
---
At [answersIT](https://answersit.com.au) we run a handful of instances in AWS for internal use. We recently faced an issue with our primary RDS server that both our accounts and sales teams use, where the EBS volumes were completely inaccessible under Windows.

As a first step to troubleshoot the issue we mounted the volumes to a Linux server to confirm that the data was still intact, it was. Rollbacks to previous snapshots / images of the instance were then attempted, but it didn't matter how far we went back the volumes were still  inaccessible - not showing in Disk Manager, or even diskpart. We were left scratching our heads and decided to open a case with Support.

Their first recommendation was to update the [PV (Paravirtual) Drivers](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.html), as it didn't look to be reporting back to the console correctly - still no dice.

Then they recommended updating the [EC2Config Service](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2config-service.html) which did the trick.

We thought we had our patching down pat using [~~Centrastage~~, ~~Autotask Endpoint Management~~, Datto RMM](https://www.datto.com/business-management/datto-rmm) and a handful of scripts, but this definitely leaves a gap in current our process and a chance to dive deeper into the AWS ecosystem using [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) - surely another post to follow!