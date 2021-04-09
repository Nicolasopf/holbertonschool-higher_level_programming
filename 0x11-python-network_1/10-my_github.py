#!/usr/bin/python3
""" Get the header value"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get("https://api.github.com/user",
                            auth=requests.auth.HTTPBasicAuth(argv[1], argv[2]))
    try:
        text = response.json()
        print(text.get('id'))
    except:
        print("Not a valid JSON")
