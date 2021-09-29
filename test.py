#!/usr/bin/env python3

from netdisco_api import NetdiscoAPI



# Instantiate API object
api = NetdiscoAPI(
  host = "http://127.0.0.1:2050/",
  user = "admindisco",
  password = "foo",
  enforce_encryption=False,
  )

device_payload = {
'q' : 'AVAYA',
'matchall' : 'false'
}
node_payload = {
'q' : '',
'partial' : True,
'vendor' : 'Vmware'
}

port_payload = {
'q' : '(Slot: 4 Port: 48)',
'partial' : True
}

vlan_payload = {
'q' : '64',
}
# search_device OK
# r=api.search_device(device_payload)
# search_node OK
# r=api.search_node(node_payload)
# search port OK
# r=api.search_port(port_payload)
r=api.search_vlan(vlan_payload)
print(r)
api.logout()
