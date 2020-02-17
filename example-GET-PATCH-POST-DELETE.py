#
# Python script to read MAC address from interface and interface statistics
#
from pprint import pprint as pp
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#
# Connect to device
#
sess=requests.Session()
# Enter username and password for the device in place of 'admin' and 'xxxxxxx'
sess.auth=requests.auth.HTTPBasicAuth('admin', 'xxxxxxx')
sess.headers.update({'Accept': 'application/yang-data+json, application/yang-data.errors+json', 'Content-type': 'application/yang-data+json'})
#
# GET the interface MAC address
#
print("\n\n############ Get GE1/0/1 interface MAC address #################\n")
print('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F1/mac-address\n')
# The url for interface mac-address is in the get below.  "/" characters in RESTCONF must be replaced with %2F
resp=sess.get('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F1/mac-address', verify=False)
pp(resp.json())

#
# GET interface statistics for GE1/0/1
#
print("\n\n############ Get Interface Statistics ##################\n")
print('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1%2F0%2F1/statistics\n')
resp=sess.get('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1%2F0%2F1/statistics', verify=False)
pp(resp.json())

#
# PATCH to configure interface description on GE1/0/1
#
print("\n\n############ Patch to configure Interface GE1/0/1 description ##################\n")
# PATCH operations to a list use a URL that points to the list.  The list entry is identified in the "data"
data = '{"GigabitEthernet": [{"name": "1/0/1", "description":"GE1/0/1"}]}'
resp=sess.patch('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet', data=data, verify=False)
pp(resp)

#
# GET interface description
#
print("\n\n############ Get Interface GE1/0/1 description ##################\n")
resp=sess.get('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1%2F0%2F1/description', verify=False)
pp(resp.json())

#
# POST to create interface Loopback100
#
print("\n\n############ POST to create interface Loopback100 ##################\n")
data = '{"Loopback": [{"name": "100", "description": "Loopback Interface 100"}]}'
resp=sess.post('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface', data=data, verify=False)
pp(resp)

#
# GET interface Loopback100 configurations
#
print("\n\n############ GET interface Loopback100 configurations ##################\n")
resp=sess.get('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100', verify=False)
pp(resp.json())

#
# DELETE interface Loopback100
#
print("\n\n############ DELETE interface Loopback100 ##################\n")
resp=sess.delete('https://172.27.255.23:443/restconf/data/Cisco-IOS-XE-native:native/interface/Loopback=100', data=data, verify=False)
pp(resp)

