---
layout: post
title:  "Parsing nginx logs using awk"
date:   2018-09-06
---

Out of the box, nginx uses the `ngx_http_log_module` using the combined format:

```
log_format combined '$remote_addr - $remote_user [$time_local]  '
            '"$request" $status $body_bytes_sent '
            '"$http_referer" "$http_user_agent"';
```

These variables are part of the `ngx_http_core_module`, and an explanation of what they return is below:

- $remote_addr – client IP address
- $remote_user – username supplied with basic authentication, generally blank
- [$time_local] – server timestamp
- "$request" – HTTP request type, path and protocol used
- $status – HTTP response returned
- $body_bytes_sent – server response size (in bytes)
- "$http_referer" – referral URL (if present)
- "$http_user_agent" – client user agent

Using awk, we can then break up each line of the log file into "columns". By default awk splits the string by the space character. Allowing us to easily report on things such as HTTP response codes:

```
awk '{print $9}' access.log | sort | uniq -c | sort -rn
126570 200
   4144 404
   1620 304
   1416 302
    891 301
    302 499
      5 206
      3 405
      1 403
      1 "-"
```

From these response codes, we can see there are 4144 404 "Not Found" responses - to determine which URLs are returning this response again we can use awk:

```
awk '($9 ~ /404/)' access.log | awk '{print $7}' | sort | uniq -c | sort -rn
   3343 /wp-content/themes/eNurse/assets/en_background1.jpg
    307 /grassblade-lrs/xAPI/statements
     53 /eshop/clearance-products
     38 /core/assets/frontend/layout/css/fancybox_overlay.png
     24 /core/assets/frontend/layout/css/fancybox_sprite@2x.png
     24 /core/assets/frontend/layout/css/fancybox_loading@2x.gif
     13 /my-account/favicon.ico
     11 /courses/favicon.ico
      8 /learninghub/favicon.ico
      7 /eshop/clearance-products?p=3
      7 /apple-touch-icon.png
      6 /professional-file/professional-file-enurse-cpd/favicon.ico
      6 /blogsarticles/favicon.ico
      6 /apple-touch-icon-precomposed.png.
      ...
```

To filter based on other response codes, just change it within the awk command, the below example would return all temporarily redirected pages based on a 301 response code:

```
awk '($9 ~ /301/)' access.log | awk '{print $7}' | sort | uniq -c | sort -rn
```

Another neat way to analyse the logs is to determine the country of origin, by performing a look up of client IP addresses using the `geoip` package:

```
awk '{ print $1 }' | sort | uniq -c | sort -rn | head -n 25 | awk '{ printf("%5d\t%-15s\t", $1, $2); system("geoiplookup " $2 " | cut -d \\: -f2 ") }'
 3213   174.129.242.xxx  US, United States
 1582   203.37.226.xxx   AU, Australia
  960   101.175.136.xxx   AU, Australia
  907   58.96.63.xxx     AU, Australia
  883   221.121.132.xxx   AU, Australia
  807   111.69.116.xxxx   NZ, New Zealand
  733   118.208.154.xxx   AU, Australia
  684   1.156.134.xxx    AU, Australia
  665   1.41.98.xxx      AU, Australia
  657   106.69.55.xxx     AU, Australia
  649   58.7.198.xxx     AU, Australia
  620   121.212.60.xxx   AU, Australia
  614   211.31.50.xxx    AU, Australia

```