---
layout: post
title:  "Removing Context Menu Items in Windows"
date:   2018-05-26 10:23:00 +1000
---
It seems like every piece of software installed adds to the context menu, here's mine after a clean installation of Windows and all the usual software.

![Context Menu after clean installation of Windows and usual software](/assets/images/removing-context-menu-items-in-windows/contextmenu.jpg)

Fortunately, it's easy enough to delete what you don't need by jumping into the registry. Just navigate to *HKEY_CLASSES_ROOT\*\shell*, and *\HKEY_CLASSES_ROOT\*\shellex\ContextMenuHandlers* and delete what you don't need.