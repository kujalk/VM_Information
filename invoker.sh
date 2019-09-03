#This is the invoker script
#Schedled to run on 08.00, 12.00, 16.00 EveryDay

#Opening Powershell session and executing Powershell script
cd /Jana_Scripts
pwsh ./create_csv.ps1

#Executing Python Script
python create_html.py

