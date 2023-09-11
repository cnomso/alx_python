"""A script that takes in a URL,
Sends a request to the URL,
and displays the value of the variable X-Request-Id
in the header ofthe response.
"""

import sys
import requests


# if __name__ == "__main__":
#     url = sys.argv[0]

#     request = requests.Request(url)
#     with requests.url(request) as resp:
#         print(dict(resp.headers).get("X-Request-Id"))


def get_x_request_id(url):
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    return x_request_id


if __name__ == "__main__":
    url = sys.argv[1]

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)
