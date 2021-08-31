# Hypervisor Example

An example Hypervisor creation and management through powerhsell and Python


## Configure virtual switch with specified IP range

Create new internal virtual switch

```powershell
New-VMSwitch -SwitchName NewSwitch -SwitchType Internal
```

Configure the NAT gateway

```powershell
New-NetIPAddress -IPAddress 192.168.0.1 -PrefixLength 24 -InterfaceAlias “vEthernet (NewSwitch)”
```

Configure network address of NAT network

```powershell
New-NetNat -Name MyNATnetwork -InternalIPInterfaceAddressPrefix 192.168.0.0/24
```

Any virtual machine that runs on the virtual switch will use an IPv4 address in the 192.168.0.0 address range


## Configure HyperVisor instance

Create VM instance with specified virtual hard drive path and attached the newly created switch

```powershell
New-VM -Name WinVM -MemoryStartupBytes 4GB -NewVHDPath c:\VM\WinVM.vhdx -NewVHDSizeBytes 10737418240  -Generation 2 -Switch NewSwitch 
```

Attach Windows ISO controller file 

```powershell
Set-VMDvdDrive -VMName WinVM -Path .\Win.iso
```

Start the newly created virtual machine

```powershell
Start-VM -Name WinVM
```

Begin installation of virtual machine


## Configure static IP address

Directly connect to the instance's powershell and enter the credentials

```powershell
Enter-PSSession -VMName WinVM 
```

Get the network interface index

```powershell
route print
```

Create and set the designated static IP address of 192.168.0.2 on the virtual machine

```powershell
New-NetIPAddress -InterfaceIndex 3 -IPAddress 192.168.0.2 
Set-NetIPAddress -InterfaceIndex 3 -IPAddress 192.168.0.2 -PrefixLength 24
```
