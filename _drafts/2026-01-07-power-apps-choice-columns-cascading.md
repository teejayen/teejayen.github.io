---
layout: post
title: "Power Apps Choice columns don't support cascading filters"
date: 2026-01-07
ai: assisted
---

If you're building a Power Apps form with cascading dropdowns backed by a SharePoint configuration list, and one of your fields is a Choice column - it won't work properly. The Choice column's default value overrides whatever you try to filter to.

## The scenario

We had a document creation form with two dropdowns:
1. **Library** - Corporate, Technical, Commercial, Calculations
2. **Document Type** - Filtered based on selected Library

Document Type was a SharePoint Choice column with "General" as the default value. The configuration list had 56 document types mapped to their valid libraries.

## What happened

No matter what Library was selected, Document Type always showed "General". The Combo Box Items property was correct:

```
Filter('Document Types Configuration', Library.Value = DataCardValue3.Selected.Value).Title
```

But the field ignored the filter and displayed its default value.

## Why Choice columns fail here

SharePoint Choice columns have:
- A fixed set of values defined at the column level
- A default value that's enforced when the form loads
- No awareness of external configuration lists

When Power Apps renders a Choice field, it pulls the choices from the column definition, not from your Items expression. The Combo Box becomes a weird hybrid - it shows your filtered items, but the default selection comes from the column's default value.

## The fix: Use a Text field with Combo Box

1. Change the SharePoint column from Choice to **Single line of text**
2. In Power Apps, use a **Combo Box** control (not Dropdown)
3. Set the Items property to filter your configuration list
4. Set the Update property to `ComboBox1.Selected.Value`

```
// Items property
Filter('Document Types Configuration', Library.Value = LibraryDropdown.Selected.Value).Title

// Update property
DocumentTypeComboBox.Selected.Value
```

Now the field is truly dynamic - filtered by your configuration list, no hardcoded defaults interfering.

## Trade-offs

**What you lose:**
- Choice column validation in SharePoint (users could theoretically enter invalid values via other means)
- The nice dropdown experience in SharePoint list views

**What you gain:**
- Actually working cascading filters
- Configuration-driven form (add new document types without modifying the column)
- Consistent behaviour between Power Apps and Power Automate

## Power Automate note

If you're updating this field via Power Automate, the text value works fine with `validateUpdateListItem`. SharePoint accepts the string even if the destination library has it as a Choice column - the endpoint handles the type conversion automatically.

```json
{
  "formValues": [
    {"FieldName": "Document_x0020_Type", "FieldValue": "Technical Report"}
  ]
}
```

## The pattern

For any configuration-driven cascading dropdown in Power Apps + SharePoint:
1. Create a configuration list with your options and their parent relationships
2. Use Text columns (not Choice) for the fields you want to filter
3. Use Combo Box controls with Filter() expressions
4. Accept that validation happens in Power Apps, not SharePoint
