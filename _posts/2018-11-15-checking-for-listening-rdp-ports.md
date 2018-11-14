---
layout: post
title:  "Checking for listening RDP ports"
date:   2018-11-15
---

There's no doubt that RDP is a useful protocol, but opening it up directly to the internet is a big no-no. Not only is there no rate limiting built in to connections, making it susceptible to bruteforce attempts - but the connection attempts themselves cause significant load on the server leading to netlogon crashing and general instability.

Listening RDP ports are one of the most common attack vectors, but fortunately securing it is rather simple. Whether you use a VPN or an RD Gateway, it doesn't matter - just as long port 3389 doesn't remain open.

The below script attempts to connect on port 3389 based on a CSV spreadsheet (requires Name, and PublicIP headers at a minimum). If it can connect, it will log it output via the console and also log it to a results CSV. As the uses `Test-NetConnection` it can also be easily amended to check other ports, or even multiple ports concurrently.


```powershell
$Customers = Import-CSV C:\temp\rdpcustomers.csv

foreach ($Customer in $Customers){
    Write-Host "Testing $($Customer.Name) - $($Customer.PublicIP) now..."
	$RDP = Test-NetConnection -ComputerName $($Customer.PublicIP) -Port 3389 -ErrorAction SilentlyContinue -WarningAction SilentlyContinue
	$Result = $null
	if($RDP.TcpTestSucceeded){
	Write-Host "Port 3389 is listening" -ForegroundColor Red
	$Result = "Listening"
	}

	else{
    Write-Host "Port 3389 is not listening"
	}
		
	if($Result -like "Listening"){
		$ResultsExport = $null
		$ResultsExport = [ordered]@{
			Customer = $Customer.Name
			PublicIP = $Customer.PublicIP
			Result = $Result
		}
		
		$ResultObject = New-Object PSObject -Property $ResultsExport
		$ResultObject | Export-Csv C:\temp\rdpcustomersresult.csv -NoTypeInformation -Append
	}

}
```