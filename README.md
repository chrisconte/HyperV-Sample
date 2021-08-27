# Hypervisor Example
An example Hypervisor creation with powershell and connection with Python

## Create Hypervisor instance with Powershell

Get the name of the virtual switch that you want the VM to use

```powershell
Get-VMSwitch  * | Format-Table Name
```
