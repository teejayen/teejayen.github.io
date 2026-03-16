---
layout: post
title: "Power Automate: Updating SharePoint Person fields requires a User ID lookup"
date: 2026-01-07
ai: assisted
---

If you're trying to update a Person field in SharePoint via Power Automate and it's silently failing or staying blank, here's what's happening: SharePoint's REST API doesn't accept the Claims string or email address directly. You need the numeric User ID.

## The symptom

You're using "Send an HTTP request to SharePoint" with `validateUpdateListItem` to update list items. Text fields work fine. Choice fields work fine. But the Person field stays stubbornly empty.

## What doesn't work

```json
{
  "formValues": [
    {"FieldName": "Owner", "FieldValue": "i:0#.f|membership|user@domain.com"}
  ]
}
```

Also doesn't work:
- Using the email address directly
- Using the `Key` property from the trigger
- Using the display name

## The fix: Two-step process

### Step 1: Look up the User ID

Add "Send an HTTP request to SharePoint" before your update action:

**Site Address:** Your site
**Method:** GET
**URI:**
```
_api/web/SiteUsers/getByEmail('@{triggerBody()?['value']?[0]?['Owner']?['Email']}')?$select=Id
```

### Step 2: Extract the numeric ID

Add a Compose action:

**Inputs:**
```
@{outputs('Get_Owner_User_ID')?['body']?['d']?['Id']}
```

### Step 3: Update using the ID field name

In your `validateUpdateListItem` call, use `OwnerId` (not `Owner`) with the numeric value:

```json
{
  "formValues": [
    {"FieldName": "OwnerId", "FieldValue": "@{outputs('Compose_-_Owner_ID')}"},
    {"FieldName": "Title", "FieldValue": "Some title"}
  ]
}
```

Note the `Id` suffix on the field name - this is required for Person fields.

## Why this is necessary

SharePoint Person fields internally store a reference to the SiteUsers collection, not the user's email or Claims identity. When you use the standard field name (`Owner`), SharePoint expects a complex object. When you use the `Id` suffix (`OwnerId`), it expects the numeric lookup value.

The `SiteUsers` collection is site-specific, so the same user can have different IDs on different sites. You must query the specific site where you're updating the item.

## Complete flow pattern

1. **Trigger** - When item created/modified in source list
2. **Get Owner User ID** - HTTP GET to `_api/web/SiteUsers/getByEmail()`
3. **Compose - Owner ID** - Extract numeric ID from response
4. **Copy file** - Copy the document
5. **Update properties** - HTTP POST to `validateUpdateListItem` with `OwnerId`

## Error handling

Consider what happens if the user doesn't exist in SiteUsers (they haven't visited the site yet). You may need to add error handling or a fallback.

## References

- [Pankaj Surti's blog post](https://pankajsurti.com/2020/10/12/how-to-update-people-field-using-send-an-http-request-to-sharepoint-in-power-automate/) - the only decent documentation I found on this
