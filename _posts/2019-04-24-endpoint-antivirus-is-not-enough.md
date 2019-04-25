---
layout: post
title:  "Why Endpoint Anti-virus is not enough to protect your business"
date:   2019-04-24
---
*This article was originally written for publishing on the company blog at [answers IT](https://answersit.com.au), and has been cross posted here.*

Simple endpoint anti-virus is no longer enough. Anti-virus uses signatures and definitions to match bad files in order to block or quarantine them. If the malware using basic obfuscation techniques such as packing, encryption, polymorphic code, or staged loading or is just new malware entirely, endpoint anti-virus generally won't have the signatures and definitions required to catch it yet.

More and more we are seeing advanced obfuscation techniques used, including process and DLL injection to link malware with a legitimate Windows executable and hide in plain sight from endpoint anti-virus.

According to the [Threat Landscape](https://www.secplicity.org/threat-landscape/?s=2019-01-01&e=2019-04-24&type=all&region=AU) reports published by WatchGuard, 82% of malware detections were classified as 0-day malware since the start of 2019.

The reality is that every network needs a full arsenal of scanning engines to protect against spyware and viruses, malicious apps and data leakage – all the way through ransomware, botnets, advanced persistent threats, and zero day malware. answers IT have partnered with WatchGuard to provide their Firebox devices to our clients through our monthly [answersMSD (Managed Security Device)](https://www.answersit.com.au/services/managed-security-devices/) service.

One of the key features of the Firebox is the Advanced Malware Pipeline which uses four different layers to scan malware before it can execute on an endpoint.

The pipeline starts with with GatewayAV which is powered by [Bitdefender](https://www.bitdefender.com/) anti-malware protection at the gateway to block known threats including viruses, trojans, spyware and ransomware in real time - if there is an existing signature for a known-bad file then it will be stopped here, otherwise it continues through the pipeline.

Next up, IntelligentAV which is built on the [Cylance](https://www.cylance.com/) artificial intelligence platform. IntelligentAV uses a combination of artificial intelligence, machine learning, and algorithmic science to defend against continuously evolving malware.

The malware will then be run through APTBlocker, powered by [Lastline](http://www.lastline.com/). Advanced Persistent Threats (APT) are a stealthy attack in which a threat actor gains access to a network and remains undetected for an extended period of time. Lastline uses a unique approach to monitor for APT, leveraging their Global Threat Intelligence Network to scan traffic metadata and payloads for variants of known threats and AI (artificial intelligence) to detect anomalies in network traffic, protocols and behaviour.

Finally, [Threat Detection & Response](https://www.watchguard.com/wgrd-products/security-services/threat-detection-and-response). TDR is a powerful collection of advanced malware defense tools that correlate threat indicators from Firebox appliances and Host Sensors to stop known, unknown and evasive malware threats. A key feature of TDR is Host Containment which will isolate endpoints from the network and prevent any further infection, and once it has cleaned up the malware only then will the device be able to connect back.

You've heard us say it before, there is no silver bullet to cybersecurity and protection. Taking a layered approach to your protection however will significantly reduce the risk of an malware infection occurring.

If you're interested to find out more about our answersMSD service and the layered protection options it provides, get in touch with your Technical Account Manager or the Service Desk team on 07 3123 7929.