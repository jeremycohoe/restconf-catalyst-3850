import requests

url = "https://10.85.134.119/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface?fields=name;speed;phys-address;admin-status;statistics/in-octets;statistics/out-octets"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic XXXXXXXXXXXXXX'
}

response = requests.request("GET", url, verify=False, headers=headers, data = payload)

print(response.text.encode('utf8'))
