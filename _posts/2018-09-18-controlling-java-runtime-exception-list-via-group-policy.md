---
layout: post
title:  "Controlling Java Runtime Exception List via Group Policy"
date:   2018-09-18
---
Since the Java Runtime 7 Update 51 release applications must now meet the requirements for the High or Very High security settings, or be part of the Exception Site List before they can be run. A few certain government website here in Australia still require the Java Runtime for logging in, such as the Tax Agent Portal and AUSKey Authentication Services - and it seems that they haven't quite got on top of keeping their certificates up to date.

While tt would be great to debate over the importance of certificates, when you have a company of 30 accountants screaming that they can't log in then unfortunately exceptions (pun intended) need to be made. In fact, it's the [recommended fix](https://www.technicalhelpdesk.com.au/s/article/Application-Blocked-by-Security-Settings) by the self-proclaimed *Technical Help Desk* for Australia.

Java Runtime stores it's exception list in a plain text file,`exception.sites`, located in %userprofile%\AppData\LocalLow\Sun\Java\Deployment\security - the file format is one site per line.

1. Copy / create the `exception.sites` file to a network location.
2. Create or edit a GPO in the most suitable Organisation Unit
3. Navigate through the GPO to Computer Configuration > Preference > Windows Settings > Files > ...
4. Configure the following options:

    **Action**: Create

    **Source file**: \\\\$server\\$path\exception.sites

    **Destination file:** %userprofile%\AppData\LocalLow\Sun\Java\Deployment\security\exception.sites
5. Revel in sadness that you're now encouraging a government organisation to not keep on top of their certificate expiries.