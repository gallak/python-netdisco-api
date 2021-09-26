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
# search_device OK
# r=api.search_device(device_payload)
r=api.search_node(node_payload)
print(r)
api.logout()
