---
layout: post
title:  "EC2 Metadata"
date:   2018-06-27 03:13:00 +1000
---
We support a huge collection of EC2 instances for clients at [answersIT](https://answersit.com.au), and sometimes all we have is access to the instance itself and not the account. The majority of instances have custom hostnames that don't always match the instance ID but fortunately Amazon provides easy access to the EC2 metadata [a couple of different ways](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html).

This can come in quite handy when writing scripts also, as you can set the metadata as variables rather than hardcoding.

You can query the metadata via shell using cURL or wget:

<pre>
root@tjn-svr-lv01:~# <b>wget -q -O - http://169.254.169.254/latest/meta-data/</b>
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
product-codes
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
</pre>

Or, if it's an Amazon Linux instance the *ec2-metadata* package comes pre-installed:

<pre>
root@tjn-svr-lv01:~# <b>./ec2-metadata --help</b>
ec2-metadata v0.1.1
Use to retrieve EC2 instance metadata from within a running EC2 instance.
e.g. to retrieve instance id: ec2-metadata -i
                 to retrieve ami id: ec2-metadata -a
                 to get help: ec2-metadata --help
For more information on Amazon EC2 instance meta-data, refer to the documentation at
http://docs.amazonwebservices.com/AWSEC2/2008-05-05/DeveloperGuide/AESDG-chapter-instancedata.html

Usage: ec2-metadata <option>
Options:
--all                     Show all metadata information for this host (also default).
-a/--ami-id               The AMI ID used to launch this instance
-l/--ami-launch-index     The index of this instance in the reservation (per AMI).
-m/--ami-manifest-path    The manifest path of the AMI with which the instance was launched.
-n/--ancestor-ami-ids     The AMI IDs of any instances that were rebundled to create this AMI.
-b/--block-device-mapping Defines native device names to use when exposing virtual devices.
-i/--instance-id          The ID of this instance
-t/--instance-type        The type of instance to launch. For more information, see Instance Types.
-h/--local-hostname       The local hostname of the instance.
-o/--local-ipv4           Public IP address if launched with direct addressing; private IP address if launched with public addressing.
-k/--kernel-id            The ID of the kernel launched with this instance, if applicable.
-z/--availability-zone    The availability zone in which the instance launched. Same as placement
-c/--product-codes        Product codes associated with this instance.
-p/--public-hostname      The public hostname of the instance.
-v/--public-ipv4          NATted public IP Address
-u/--public-keys          Public keys. Only available if supplied at instance launch time
-r/--ramdisk-id           The ID of the RAM disk launched with this instance, if applicable.
-e/--reservation-id       ID of the reservation.
-s/--security-groups      Names of the security groups the instance is launched in. Only available if supplied at instance launch time
-d/--user-data            User-supplied data.Only available if supplied at instance launch time.
</pre>