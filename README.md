# Hypervisor Example
An example Hypervisor creation with powershell and connection with Python

## Create Hypervisor instance with Powershell

Get the name of the virtual switch that you want the VM to use

```powershell
Get-VMSwitch  * | Format-Table Name
```

Create instance swith selected virtual switch

```powershell
New-VM -Name Win10VM -MemoryStartupBytes 2GB -BootDevice VHD -VHDPath .\VMs\Win10.vhdx -Path .\VMData -Generation 2 -Switch ExternalSwitch
```

Start the newly created virtual machine

```powershell
Start-VM -Name Win10VM
```

Connect to the virtual machine with VMConnect

```powershell
VMConnect.exe
```
