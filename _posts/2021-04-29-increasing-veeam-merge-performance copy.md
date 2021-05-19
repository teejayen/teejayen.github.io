---
layout: post
title:  "Increasing Veeam merge performance"
date:   2021-04-29
---

Slow merge performance in Veeam? Add in this DWORD and it'll run one thousand times better:

```
Name: CloudConnectQuotaAllocationMode
Path: HKEY_LOCAL_MACHINE\SOFTWARE\Veeam\Veeam Backup and Replication\
Type: DWORD
Default value: 0 -> 1
```

This changes the mechanism from limiting 512MB allocation every 15 seconds, to providing on tap quota Veeam needs to perform the merge.

## References

- [How to increase your Veeam backup performance on VCD by 10+x](https://vcloudvision.com/2021/02/22/how-to-increase-your-veeam-backup-performance-on-vcd-by-10x/)
- [Really slow merging to cloud storage](https://forums.veeam.com/veeam-backup-replication-f2/really-slow-merging-to-cloud-storage-t65843.html)