---
layout: post
title:  "My first flag! BSides Brisbane 2019 CTF - RFID"
date:   2019-07-08
---

**Category:** IoT

**Points:** 250

**Solves:** 3

**Story:** This security gate controls access to a manager-only area of the office! One of the managers is very paranoid, so he has a script setup to rotate his keycard every 60 seconds.

**Scope:** You need to hijack a card to gain swipe access to the managers area.

![IoT Village: Access Control](/assets/images/bsides-brisbane-2019-ctf-rfid/accesscontrol.jfif)
![Nano and Reader](/assets/images/bsides-brisbane-2019-ctf-rfid/nanoreader.jpg)

The table had a selection of various RFID / NFC cards, as well as [Arduino Nano clones](https://www.diymore.cc/products/mini-usb-nano-v3-0-atmega328-micro-controller-16m-5v-ch340g-board-for-arduino) and [RC522 proximity modules](https://www.diymore.cc/products/2pcs-rc522-card-read-antenna-rf-rfid-reader-ic-card-proximity-module-mfrc-522-key).

I was able to get the RC522 proximity module properly interfacing with the Nano clone after finding a [handy pin out diagram on the Ardruino Stack Exchange](https://arduino.stackexchange.com/questions/47185/arduino-nano-rc522-w5500-ethernet-module) and the [MFRC522 Arduino Library which is maintained by miguelbalboa](https://github.com/miguelbalboa/rfid).

I performed some research into the NXP MIFARE Classic 1K cards, and after reviewing the [datasheet](https://www.nxp.com/docs/en/data-sheet/MF1S70YYX_V1.pdf) I determined that byte 9 could have user data written to them. I tried reading a couple of the cards using the [DumpInfo](https://github.com/miguelbalboa/rfid/tree/master/examples/DumpInfo), but couldn't find any useful data on them or they were blank.

I noticed when scanning an invalid card against the reader to actuate the gate that it would give an Access Denied error, and then show a timestamp. I struggled for a good 30 minutes trying to write the timestamp data (in hex format) using Arduino IDE and the example code.. I almost conceded defeat but recalled that my phone (Samsung S10) can read and write NFC, so as a last ditch effort I download [NFC Tools](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc) from the Google Play Store.

Using NFC Tools I was able to read AND write data to the card easily, and most importantly quickly - as I only had 60 seconds between writing and reading the card.

After a few attempts to get the timestamp in the correct format and written to the card, I was able to open up the gate and now had my very first flag: flag{j98Ndgk7G3}
