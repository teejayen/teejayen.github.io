---
layout: post
title: "Auditing macro files across M365 with Microsoft Graph"
date: 2026-01-07
ai: assisted
---

If you're working on Essential Eight compliance (or just want to know where your macro-enabled files live), here's how to audit your entire SharePoint and OneDrive environment using Microsoft Graph.

## The approach

Microsoft Graph's Search API can query across all SharePoint sites and OneDrive accounts in your tenant. We search for each macro file extension and export the results.

## The script

```powershell
# audit-macro-files-graph.ps1
Connect-MgGraph -Scopes "Sites.Read.All"

$extensions = @("xlsm", "docm", "dotm", "xlam", "pptm", "potm", "ppam", "sldm")
$allResults = @()

foreach ($ext in $extensions) {
    Write-Host "Searching for .$ext files..."

    $body = @{
        requests = @(
            @{
                entityTypes = @("driveItem")
                query = @{
                    queryString = "filetype:$ext"
                }
                from = 0
                size = 500
            }
        )
    } | ConvertTo-Json -Depth 10

    $response = Invoke-MgGraphRequest -Method POST `
        -Uri "https://graph.microsoft.com/v1.0/search/query" `
        -Body $body -ContentType "application/json"

    foreach ($hit in $response.value[0].hitsContainers[0].hits) {
        $allResults += [PSCustomObject]@{
            Name = $hit.resource.name
            Extension = $ext
            WebUrl = $hit.resource.webUrl
            LastModified = $hit.resource.lastModifiedDateTime
            CreatedBy = $hit.resource.createdBy.user.displayName
            Size = $hit.resource.size
        }
    }
}

$allResults | Export-Csv -Path "macro-audit.csv" -NoTypeInformation
Write-Host "Found $($allResults.Count) macro files"
```

Note: The search API returns max 500 results per request. For larger environments, implement pagination using the `from` parameter.

## What we found

Running this across our ~100 person engineering firm:

| Extension | Count | Description |
|-----------|-------|-------------|
| .xlsm | 2,339 | Excel macro workbooks |
| .docm | 114 | Word macro documents |
| .dotm | 17 | Word macro templates |
| .xlam | 5 | Excel add-ins |
| .pptm | 2 | PowerPoint macro presentations |
| **Total** | **2,477** | |

Of the 2,477 files, only 1,860 were unique filenames. The remaining 617 were templates deployed multiple times across projects - things like drawing registers, transmittal forms, and engineering calculation templates.

## Analysis script

To identify templates vs one-off files:

```powershell
$macros = Import-Csv "macro-audit.csv"

# Group by filename to find templates
$grouped = $macros | Group-Object Name |
    Where-Object { $_.Count -gt 1 } |
    Sort-Object Count -Descending

Write-Host "Templates deployed multiple times:"
$grouped | Select-Object Count, Name -First 20 | Format-Table
```

## The compliance angle

If you're doing this for Essential Eight ML2, here's what I learned the hard way: **code signing is ML3, not ML2**.

The actual ML2 requirements for macros are:
- Microsoft Office macros are disabled for users who don't need them
- Microsoft Office macros in files from the internet are blocked
- Antivirus scanning of macros is enabled
- Microsoft Office macro security settings cannot be changed by users

All achievable with Intune policies and ASR rules. No signing infrastructure required.

Use the audit data to identify which users actually need macro access (for your "Macro Users" security group), not to prioritise signing efforts.

## References

- [Microsoft Graph Search API](https://learn.microsoft.com/en-us/graph/api/resources/search-api-overview)
- [ACSC Essential Eight Maturity Model](https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight/essential-eight-maturity-model)
