#!/usr/bin/env python3
import requests

# Replace the ip address with the local address of your ETA heating
url='http://192.168.178.46:8080'

# This resource returns the version of the API.
apiversion='/user/api'
# This resource identifies the menu tree which you can see on the touch display in the tree view.
menutree='/user/menu'
# This resource identifies a variable in the CAN system.
variable='/user/var'
# This resource identifies a set of variables. It allows you to define your own named variable
# set which acts as a container for different single variables. Having once created a variable
# set you can add or remove arbitrary variables from the CAN system to this set.
variableset='/user/vars'
# This resource identifies the active errors in the CAN system.
errors='/user/errors'

response = requests.get(url+apiversion)
print(response.status_code)

if response.ok:
    print(response.content)
    
    