"""
Takes your Github credentials (username and password) and
uses the Github API to display your id
"""
import requests
from sys import argv


def get_github_id(username, token):
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()
        print(f"Your GitHub ID is: {data['id']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except ValueError as json_err:
        print("Not a valid JSON")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    get_github_id(username, token)
