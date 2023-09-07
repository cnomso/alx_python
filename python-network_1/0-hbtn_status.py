"""fetches the details from
    https://alu-intranet.hbtn.io/status
"""


import requests
    """fetches
    https://alu-intranet.hbtn.io/status
    """
with requests.get("https://alu-intranet.hbtn.io/status") as response:
    """fetches
    https://alu-intranet.hbtn.io/status
    """
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
