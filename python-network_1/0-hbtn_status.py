"""
Python script that fetches a URL
"""

import requests

req = requests.get("https://alu-intranet.hbtn.io/status")

print("Body response:")
print("\t- type: {}".format(type(req)))
print("\t- content: {}".format(req))
# print("\t- utf8 content: {}".format(req.decode(encoding="utf-8")))
