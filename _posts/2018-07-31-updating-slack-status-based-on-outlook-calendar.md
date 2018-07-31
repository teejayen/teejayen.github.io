---
layout: post
title:  "Updating Slack Status based on Outlook Calendar"
date:   2018-07-31 23:05:00 +1000
---

I used to pride myself on always being available to answer questions from the team on Slack, but found that this was seriously detrimental to getting my own work done - so I have been trying out [time blocking](http://calnewport.com/blog/2013/12/21/deep-habits-the-importance-of-planning-every-minute-of-your-work-day/) over the past couple of weeks, and utilising *Do Not Disturb* on Slack a fair bit.

To keep others in the loop I've automated updating Slack status based on my current time block in my Outlook calendar. It's a [quick and dirty PowerShell script](https://github.com/teejayen/powershell-snippets/blob/master/Set-SlackStatus.ps1), but for my needs it works quite well.

```shell
$Username = ""
$Password = ""
$Credentials = New-Object System.Management.Automation.PsCredential($Username,(ConvertTo-SecureString $Password -AsPlainText -Force))

$SlackToken = ""

$CalendarItem = Invoke-RestMethod -Uri "https://outlook.office365.com/api/v1.0/users/$UserName/calendarview?startDateTime=$((Get-Date).AddHours(-10))&endDateTime=$((Get-Date).AddHours(-10))" -Credential $Credentials | foreach-object{ $_.Value } | Select-Object -ExpandProperty Subject

$Payload = @{"status_text" = $CalendarItem;"status_emoji" = ":spiral_calendar_pad:"}
$JSON = ConvertTo-Json $Payload

Invoke-WebRequest -Method Post -Uri https://slack.com/api/users.profile.set?token=$SlackToken"&"profile=$JSON
```