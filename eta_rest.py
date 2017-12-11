#!/usr/bin/env python3
import requests

url='http://192.168.178.46:8080/user/api'

response = requests.get(url)
print(response.status_code)