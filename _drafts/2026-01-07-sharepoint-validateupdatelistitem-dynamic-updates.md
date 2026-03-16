---
layout: post
title: "SharePoint ValidateUpdateListItem for dynamic Power Automate updates"
date: 2026-01-07
ai: assisted
---

Power Automate's "Update file properties" action has a frustrating limitation: the library name is a static dropdown. You can't use expressions. If your flow needs to update files across multiple libraries dynamically, you're stuck.

Unless you use `ValidateUpdateListItem`.

## The problem

We had a flow that copied documents to different libraries based on user selection - Technical-Working, Corporate-Working, Commercial-Working, etc. After copying, we needed to set metadata. But "Update file properties" requires picking one specific library from a dropdown.

The alternative - a Switch statement with four identical update actions - is maintenance hell.

## The solution

Use "Send an HTTP request to SharePoint" with the `ValidateUpdateListItem` endpoint. It accepts the library name as an expression.

**Site Address:** Your site

**Method:** POST

**URI:**
```
_api/web/lists/GetByTitle('@{variables('TargetLibrary')}')/items(@{outputs('Copy_file')?['body/ItemId']})/ValidateUpdateListItem
```

**Headers:**
```
Content-Type: application/json;odata=verbose
```

**Body:**
```json
{
  "formValues": [
    {"FieldName": "Document_x0020_Type", "FieldValue": "@{triggerBody()?['DocumentType']}"},
    {"FieldName": "Title", "FieldValue": "@{triggerBody()?['Title']}"},
    {"FieldName": "Discipline", "FieldValue": "@{triggerBody()?['Discipline']}"}
  ],
  "bNewDocumentUpdate": true
}
```

## Key details

### Library name format

`GetByTitle()` uses the **display name** (what you see in Site Contents), not the URL path:
- Display name: `Technical-Working`
- URL path: `TechnicalWorking`

Use the display name in your expression.

### Field name encoding

Spaces in field names become `_x0020_`:
- "Document Type" → `Document_x0020_Type`
- "Project Number" → `Project_x0020_Number`

### Type conversion

`ValidateUpdateListItem` handles type conversion automatically:
- Text to Choice: Works if the value matches exactly
- Text to MultiChoice: Works (semicolon-separated for multiple values)
- Text to Number: Works

This means your source list can use Text fields (for flexibility) while destination libraries use Choice fields (for validation).

### Person fields

Person fields need special handling - use the `Id` suffix and numeric User ID:

```json
{"FieldName": "OwnerId", "FieldValue": "42"}
```

See my other post on Person field updates for the full pattern.

### ETag for concurrency

If you need optimistic concurrency (preventing overwrites), include the ETag:

```json
{
  "formValues": [...],
  "bNewDocumentUpdate": false,
  "checkInComment": "",
  "properties": {
    "__metadata": {"type": "SP.Data.DocumentsItem"},
    "OData__UIVersionString": "@{outputs('Get_file_metadata')?['body/{VersionNumber}']}"
  }
}
```

Note: ETag values from SharePoint include quotes that get escaped in JSON. Use a Compose action with `replace()` to strip them first.

## Debugging

Add a Compose action before the HTTP request with your complete body. Run the flow, check the Compose output. Common issues:
- Escaped quotes in strings
- Null values where strings expected
- Field names not matching (check internal name vs display name)

## When to use this

- Dynamic library selection based on user input or conditions
- Bulk operations across multiple libraries
- Complex metadata updates that exceed "Update file properties" capabilities
- Any scenario where you need the library name to be an expression

For simple, single-library flows, "Update file properties" is fine. But once you need flexibility, `ValidateUpdateListItem` is the way.
