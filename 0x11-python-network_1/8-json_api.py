#!/usr/bin/python3
""" Get the header value"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("No result")
        exit()
    response = requests.post(
        "http://110bb9ddcf0f.b594c0bb.hbtn-cod.io:5000/search_user",
        data={"q": argv[1]})
    text = response.json()
    print("[{}] {}".format(text['id'], text['name']))
