"""
Sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""


import requests
import sys


def fetch_and_display(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)

    except requests.exceptions.HTTPError as http_err:
        print(f"Error code: {response.status_code}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display(url)
