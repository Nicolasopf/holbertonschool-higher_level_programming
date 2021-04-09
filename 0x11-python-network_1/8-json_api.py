#!/usr/bin/python3
""" Get the header value"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": q})

    try:
        text = response.json()
        if bool(text) is False:
            print("No result")
        else:
            print("[{}] {}".format(text['id'], text['name']))
    except:
        print("Not a valid JSON")
