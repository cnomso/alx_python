"""fetches
    https://alu-intranet.hbtn.io/status
"""


import urllib.request
import requests

with requests.get("https://alu-intranet.hbtn.io/status") as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
