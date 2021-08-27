import json
import wmi

#Import request data from JSON file
with open('request-data.json',) as jsonfile:
    data = json.load(jsonfile)

#Establish initial connection to server
connection = wmi.connect_server(server=data.get("address"), namespace=r"root\virtualization", user=data.get("userid"), password=data.get("password"))
wmiServerConnection = wmi.WMI(wmi=connection)

#Get the system object
vmSystem = wmiServerConnection.Msvm_ComputerSystem(ElementName=data.get("name"))

#Get the management service object
vmManagement = wmiServerConnection.Msvm_VirtualSystemManagementService()

#Get the objects associated with the VM
vmObjects = vmSystem[0].associators(wmi_result_class="Msvm_VirtualSystemSettingData ")

#Apply the snapshot
for singleVmObject in vmObjects:    
    if(singleVmObject.SettingType == 5 and singleVmObject.ElementName == "snapshotName"):
        retVal = vmManagement[0].ApplyVirtualSystemSnapshotEx(vmSystem[0].path(), singleVmObject.path())
