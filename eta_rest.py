#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import requests
import xml.etree.ElementTree as ET

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

tempOutside='/40/10241/0/0/12197'
system='/40/10241'

request = url+menutree
response = requests.get(request)
if response.ok:
    parser = ET.XMLParser(target=ET.TreeBuilder(), encoding='UTF-8')
    root = ET.XML(response.content, parser=parser)
    for child_one in root:
        for child_two in child_one:
            if child_two.attrib['name']=='Lager':
                for child_three in child_two:
                    if child_three.attrib['name']=='Vorrat':
                        vorrat = child_three.attrib['uri']
            #if child_two.attrib['name']=='Sys':
            #    for child_three in child_two:
            #        for child_four in child_three:
            #            print(child_four.attrib['name'])
            #            if child_four.attrib['name'] == 'Au?entemeperatur':
            #                print('child four')
            #                tempOutside=child_tree.attrib['uri']
            #        print(child_three.tag)
                
request = url+variable+vorrat
response = requests.get(request)
if response.ok:
    parser = ET.XMLParser(target=ET.TreeBuilder(), encoding='UTF-8')
    root = ET.XML(response.content, parser=parser)
    size = int(root[0].text)
    print('Der aktuelle Lagerstand betraegt',size/10, 'kg')
    
    


