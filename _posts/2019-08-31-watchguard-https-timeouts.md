---
layout: post
title:  "WatchGuard HTTPS timeouts - turn off OCSP validation!"
date:   2019-08-31
---

We (answers IT) have had a few clients with WatchGuard Firebox devices report issues with some websites timing out when loading, it didn't happen all the time, and subsequent reloads seemed to work fine. Trawling through the Traffic Logs didn't seem to point to any specific issue occuring, there was certainly no issues with Denys occuring either.. so a case with logged with support.

Turns out it was due to [Online Certificate Status Protocol (OCSP) Validation](https://en.wikipedia.org/wiki/Online_Certificate_Status_Protocol) timing out. If OCSP Validation is enabled, there can be a delay of several seconds when the Firebox requests a response from the OCSP server. The Firebox does retain between 300 and 3000 OCSP responses in a cache to improve performance for frequently visited sites - which explains why the reload worked fine.

As most browsers (well, except for Chrome which uses it's own mechanisms) will perform OCSP Validation it's kind of redundant having the Firebox do it also. Disabling it in the TLS Profile is a couple of clicks, and fixed the timeout issues instantly. Further information about configuring the TLS profiles is available from the [WatchGuard Help Center](https://www.watchguard.com/help/docs/help-center/en-US/Content/en-US/Fireware/proxies/general/tls_profiles_about_c.html).

