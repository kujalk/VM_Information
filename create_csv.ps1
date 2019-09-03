#Powershell Script to get details from each server and store the results in CSV
#Developer - Janarthanan
#Date - 28/8/2019

Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$pwdtext=Get-Content /Jana_Scripts/secure_pwd.txt
$pwdoriginal=$pwdtext | ConvertTo-SecureString

$user='user name'
$credential=New-Object System.Management.Automation.PSCredential -ArgumentList $user,$pwdoriginal



#Function
function get-csv
{
param([string]$server_name)
write-host "Working on $server_name"

Connect-VIServer -Server $server_name -Credential $credential
Get-VM | Select-Object Name,@{N="Power State";E={($_.PowerState)}}, @{N="IPV4 Address";E={($_.guest.IPAddress -like "19*")}},@{N="Num of CPUs";E={($_.NumCPU)}},@{N="Memory (GB)";E={($_.MemoryGB)}},@{N="Hard Disk (GB)";E={@([math]::Round($_.ProvisionedSpaceGB)-$_.MemoryGB)}}| Export-Csv "/Jana_Scripts/csv_files/$server_name.csv" -NoTypeInformation
Disconnect-VIServer -Server $server_name -force -Confirm:$false
}

#Server IP Addresses
$server_list=@("192.168.2.101","192.168.2.102","192.168.2.103")

foreach ($ser in $server_list)
{
get-csv -server_name $ser
}

Exit


