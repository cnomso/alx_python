"""
Python script that fetches https://alu-intranet.hbtn.io/statu
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alu-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        html = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
