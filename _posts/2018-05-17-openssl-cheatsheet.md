---
layout: post
title:  "OpenSSL Cheatsheet"
date:   2018-05-17 23:05:00 +1000
---

Having to deal with the recent [DigiCert Revocation & Symantec Distrust *fiasco*](https://www.trustico.com.au/news/2018/digicert-symantec-statement/set-the-record-straight.php) led to an opportunity to become more familiar with OpenSSL.

Fortunately only 18 certificates (out of around 45) had to be replaced, unfortunately a client's *monster* certificate which has 69 SANs was amongst the 18!

Below is a handful of commands which I used frequently with the replacement certificates, I couldn't find a concise list which outlined them well so thought why not post about it.

### Create private key

```shell
openssl genrsa -out private.key 2048
```

### Verify private key

```shell
openssl rsa -in private.key –check
```

### Generate CSR with existing private key

```shell
openssl req -out csr.csr -key private.key -new
```

### Verify CSR

```shell
openssl req -text -noout -verify -in csr.csr
```

### Verify certificate

```shell
openssl x509 -text -noout -in cerificate.cer
```

### Verify certificate chain installed on server

```shell
openssl s_client -showcerts -host example.com -port 443
```

### Convert certificate and private key to PFX container

```shell
openssl pkcs12 -export -out certificate.pfx -inkey private.key -in certificate.cer -chain intermediate.cer
```

### Extract private key from PFX

```shell
openssl pkcs12 -in certificate.pfx -nocerts -out private.pem
```

### Remove passphrase from private key

```shell
openssl rsa -in private.pem -out private.key
```