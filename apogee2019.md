---
title: WatchGuard Apogee 2019
permalink: apogee2019/
layout: page
sitemap:
  exclude: 'yes'
---
# WatchGuard Apogee 2019

## Day 1

- Trusted Wireless Environment - sign the petition, promote on LinkedIn
- Look at setting up WIPS with Ubiquiti AP, or even start selling AP125 instead through MSSP
- Dimension/Visibility is now in WatchGuard Cloud - released yesterday, update feature key on devices to start using on Basic/Total Security devices
- Moving to better "subscription" based billing, pay WatchGuard directly and they will order through distributor and apply to our account - orchestrated by RestAPI (coming soon)
- WatchGuardONE Partner - moving towards specific specialisations - Security, AuthPoint, Wireless (but best to focus on all three)
- AuthPoint MFA is now available for the partner portal
- Significant R&D going in to DNSWatch/DNSWatchGo, aim is to provide full subscription stack when devices are off the network

### Inside The World of Criminal Hackers

- Secplicity provides Threat Landscape reports, published quarterly -it's opt-in to send details from Firebox devices and they correlate this data in to the report (approximately 45,000 Fireboxes reporting right now)
- Threat Landscape reports can be filtered based on location, timeframe and shared with clients (see https://www.secplicity.org/threat-landscape/?s=2019-01-01&e=2019-03-31&type=all&region=AU)
- Cryptojacking has become increasing popular, and can be mitigated using IntelligentAV
- IoT botnets are evolving, Mirai, Torri, Omni
- Credential stuffing is the new thing, user authentication is a huge target
- Layered defense is not new - think building security (fence, cameras, walls, security guards, mantraps, safes), tank armour (nitride ceramic coating, beryllium-copper-nickel alloy, titanium-boron fibres composite, titanium dissipative foam, etc. etc.), bulletproof vest (layer upon layer of kevlar)
- Advanced Antimalware Pipeline - GatewayAV > IntelligentAV > APTBlocker > Threat Detection & Response
- SSLv2/v3 iscompletely deprecated in 12.4, only TLS1.1, 1.2, and 1.3 available

### WatchGuard relies on joint success:

- Embrace WatchGuard Mission
- Embrace the portfolio
- Embrace go-to market strategy
- If not, why not.. tell your account manager!

### The Hedgehog Concept from Good to Great
You can either be a fox, or a hedgehog - WatchGuard are being a hedgehog.

“The Hedgehog and the Fox” describes how the world is divided into two types. The fox knows many things. The fox is a very cunning creature, able to devise a myriad of complex strategies to sneak attack upon hedgehog. The hedgehog knows one big thing, rolling up into a perfect little ball thus becoming a sphere of sharp spikes, pointing outward in all directions. The hedgehog always wins despite the different tactics the fox uses.

- What are you passionate about? Security
- What can you be the best in the world at? Simplicity
- What drives your economic engine? Channel

### Product Team are Maniacal about Simplicity

- Join the BETA program to test and provide feedback.
- Attend monthly product webinars, or listen to the recordings and provide feedback.
- Provide feedback to May about anything the product team should know about!

## Day 2 - Technical Track

### AuthPoint

2FA is not MFA:

- Something you know (password / PIN)
- Something you have (token, mobile phone)
- Something you are (fingerprint / face)

AuthPoint supports both online & offline MFA:

- Push-Based Authentication (see who is trying to authenticate to what, and where from - can also block)
- QR Code-Based Authentication (use camera to read unique, encrypted QR code with a challenge that can only be read by the app)
- TOTP (dynamic, time-based on-time password manually typed in)

Supports SAML, with JITP coming soon.

Google Authenticator / Authy - is it a competitor?

- No authentication back end - if you want to use it, you have to develop it
- No management interface - no user provisioning, synchronisation, logs, encrypted
- No direct integration with firewalls for VPN - need to build your own RADIUS
- No integration with business cloud applications (Salesforce, Office 365, etc)
- No protection for computer logon

#### Roadmap for AuthPoint

- Q1
  - Focus on agents
  - MacOS Logon app
- ADFS Agent

- Q2
  - MFA for WatchGuard ID
  - Risk-Based authentication
  - Safe locations for web SSO
  - AuthPoint agent for Windows, including RDP and RDG support
  - Hardware tokens

### WatchGuard Cloud

https://p.widencdn.net/rutrxh/Tech_Brief_WGCloud

- Fully built on AWS, following WAF
- Fully redundant across three regions, and within those up to four availability zones

- Multi-Tenant Architecture
  - Complete segregation
  - Scales to thousands of companies
  - Unlimited number of companies, and unlimited number of users per company
  - Manage multiple organisations from one interface
  - Operators onboarded at lowest permission level

#### WatchGuard Cloud Visibility

- Firebox T- and M- series, Firebox Cloud, and FireboxV
- Basic Security Suite or Total Security Suite (MSSP / NFR included)
- Fireware 12.0.1 or newer
- Basic Security Suite - 1 day data retention
- Total Security Suite - 30 days data retention
- Add-on licences avaialble (sold in 1 month increments, up to 3 years)
- WatchGuard Cloud handles SN swap for any RMAS
- Customers can move data retention between devices, without needing to log a support companies

### DNSWatchGO

- By 2021, 27% of network traffic for the average company will bypass the network perimeter entirely.
- Protects end users from phishing, and redirects to a training page (soon to be refreshed)
- Complements RED and WebBlocker to block malicious threats
- All blocks will alert, and the discussion is directly with one of WatchGuard's threat researchers

There's a hole in your umbrella: https://medium.com/alphasoc/theres-a-hole-in-your-umbrella-960ab0cc7e6e
WatchGuard blocked 61% of URLS, where as Cisco Umbrella only blocked 2%!

### 2019 Roadmap

#### Fireware 12.4 and 12.5

- SD-WAN is now a standard feature, will include MPLS and BOVPN
- Failover based on jitter / latency / loss
- Can monitor all Trusted / Optional / Custom interfaces

Logging

- Support for up to three syslog servers
- Useful for local syslog and SIEM system

Clientless VPN via access portal

- Secure reverse proxy for the SMB
- Includes HTML5 shell / RDP / web applications
- Internal web apps can be accessed from internet and protected by security features (TLS / MFA / SAML)
- User / Group based permissions and control
- SSO options to forward login credentials
- Web apps share the same port (443 by default) in external URLS

WebBlocker override with Active Directory

- Rather than a master password
- Can be configured per category
- Per user / per group options

T35-R (Rugged)

- Same processor as T35
- Rugged enclosure with DIN rail
- IP64 (fully dust proof / splash resistant)
- Fanless
- DC power (12V to 48V)
- Temperature range of -40 to 60 degrees celsius

#### Fireware OS Roadmap

- 12.4 (Q1 2019)
  - SD-WAN
  - WebBlocker "warn" options
  - IPv6 BOVPN
  - TLS 1.3 encryption and support

- 12.5 (Q2 2019)
  - Access portal for on-prem apps
  - WebBlocker AD override, customised warning message
  - Netflow on egress
  - VPN AWS / Azure config script update
  - Firecluster performance improvements

- 12.6 (Q3 2019)
  - SD-WAN - bandwidth quota per month (4G)
  - Layer 2 tunnel from AP to Firebox (EoGREoIPSec)
  - Updated IPS engine
  - SSL client refactor

- Q4 2019 + beyond
  - SD-WAN MacOS
  - IPv6 Multi-WAN
  - IPS Signature Rollback
  - Deep AuthPoint integration
    - Gateway on Firebox  
    - Connect information to Firebox
    - TOTP for WSM

### Threat Detection & Response Roadmap

- Q1 2019
  - Network correlation
  - 0-day mitigation
  - Process identification
  - Built in AV exclusions for common vendors

- Q2 2019
  - WGC Integration - Accounts / RBAC
  - Coordinated VPN access control w/ host sensor
  - Combined system tray (TDR / DNSWatchGO)
  - YARA rules
  - DLL injection behavious

- Q3 2019
  - WGC Integration - Logs
  - Insightful Visibility
  - Behaviour Detection Visualisation (HRP)

- Q4 2019 + beyond
  - WGC Integration - Reports
  - ThreatSync syslog
  - Unified Threat Intelligence
    - Lastline query service
    - Hash Sharing TF & WL
  - Synchronisation Application Control w/ Host sensor
  - APT Blocker CLEANs to Whitelist
  - Insightful Visbility Insightful
    - Behaviour Sequencing
    - Sensor Deployment
  - Save Filter by session / users
  - Non-AD bulk host sensor deployment

### WatchGuard Cloud Roadmap

- Q1 2019
  - Core Dashboards & Reporting
  - Firecluster
  - Alerts & Notfications
  - Data retention

- Q2 2019
  - Fireware upgrades
  - Remote reboot
  - RapidDeploy II
  - Synchronise feature keys

- Q3 2019
  - Maintenance broadcast
  - Feature toggle
  - Device Grouping
  - Custom QBR Reporting
  - Domain / Host Name Resolution
    - Static mapping in WGC
    - DHCP information

- Q4 2019
  - Reporting by user group
  - Reporting catch up
  - Automated partner alerts
  - Branding and customisation
  - Custom query reporting
  - Custom dashboards

### Wireless

- Rogue AP - Allows attackers to bypass perimeter security
- "Evil Twin" AP - Lures users to connect to it as to spy on traffic, steal data and infect systems
- Neighbor AP - Risks infection from connecting to other SSIDs while in range of the authorised AP
- Rogue Client - Delivers malware payloads to the network after connecting to malicious APs
- Ad-Hoc Network- Uses peer to peer connects to evade security controls and risks exposure to malware
- Misconfigured AP - Opens network to attack as a result of configuration errors

WatchGuard is the only vendor to detect and prevent six known wi-fi threats while maintaining performance, based on Miercom report.

#### Wireless "6"

- Wireless 4 is 11n
- Wireless 5 is 11ac
- Wireless 6 is 11ax
  - 4x better throughput
  - 40% faster
  - Longer battery life
  - 5GHz AND 2.4GHz
  - OFDMA (Orthogonal frequency-division multiple access) up / down

### APAC breakout

- Red for Red is back (trade up to 3 year TSS, get appliance for free - not MSSP)

**Under the counter offer**

- Trade in offer for table top appliances
- Trade in for 3 year TSS, get additional year
- Stacks with deal registration, requires special bid

Majority of concerns from customers from survey can be mitigated using authentication controls (AuthPoint).