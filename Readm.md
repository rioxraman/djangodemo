(Get-Content -Path "$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt" -TotalCount 100) > last_100_commands.txt
