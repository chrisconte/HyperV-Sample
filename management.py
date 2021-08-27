import json
import wmi

with open('request-data.json',) as jsonfile:
    data = json.load(jsonfile)

conn = wmi.WMI(data.get("address", user=data.get("userid"), password=data.get("password))
#Print all properties
def properties():
    wmi.WMI().Win32_Process.methods.keys()

#Print all methods
def methods():
    wmi.WMI().Win32_Process.properties.keys()

#List processes

def processList():
    for process in conn.Win32_Process():
        print("ID: {0}\nHandleCount: {1}\nProcessName: {2}\n".format(process.ProcessId, process.HandleCount, process.Name))

#Start target service
def startService():
    for s in conn.Win32_Service(StartMode="Auto", State="Stopped"):
        if 'Update' in s.Name:
            result, = s.StartService()
            if result == 0:
                print("Successfully started service:", s.Name)


#Get local users and groups
def usersGroups():
    for group in conn.Win32_Group():
        print(group.Caption)
    for user in group.associators(wmi_result_class="Win32_UserAccount"):
        print(" [+]", user.Caption)


usersGroups()
