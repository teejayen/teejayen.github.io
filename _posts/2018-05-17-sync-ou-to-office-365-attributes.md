---
layout: post
title:  "Sync OU information to Office 365 custom attributes"
date:   2018-05-17 17:17:00 +1000
published: false
---
Wanted to get this documented before leaving for the day, so will update the post in due course with further information.

```powershell
New-ADSyncRule 
-Name 'In from AD - OU Custom Attributes'
-Identifier 'e1107c73-5633-47c7-aa8e-47d5e0927720'
-Description ''
-Direction 'Inbound'
-Precedence 40
-PrecedenceAfter '00000000-0000-0000-0000-000000000000'
-PrecedenceBefore '00000000-0000-0000-0000-000000000000'
-SourceObjectType 'user'
-TargetObjectType 'person'
-Connector '13348ad5-ad40-4d01-a719-098cc4d43e76'
-LinkType 'Join'
-SoftDeleteExpiryInterval 0
-ImmutableTag ''
-OutVariable syncRule


Add-ADSyncAttributeFlowMapping 
-SynchronizationRule $syncRule[0]
-Source @('dn')
-Destination 'extensionAttribute10'
-FlowType 'Expression'
-ValueMergeType 'Update'
-Expression 'CStr([dn])'
-OutVariable syncRule


Add-ADSyncAttributeFlowMapping 
-SynchronizationRule $syncRule[0]
-Source @('dn')
-Destination 'extensionAttribute11'
-FlowType 'Expression'
-ValueMergeType 'Update'
-Expression 'DNComponent(CRef([dn]),2)'
-OutVariable syncRule


Add-ADSyncAttributeFlowMapping 
-SynchronizationRule $syncRule[0]
-Source @('dn')
-Destination 'extensionAttribute12'
-FlowType 'Expression'
-ValueMergeType 'Update'
-Expression 'DNComponent(CRef([dn]),3)'
-OutVariable syncRule


Add-ADSyncRule 
-SynchronizationRule $syncRule[0]


Get-ADSyncRule 
-Identifier 'e1107c73-5633-47c7-aa8e-47d5e0927720'
```