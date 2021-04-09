#!/usr/bin/python3
""" Get the header value"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": argv[2]}).encode("utf-8")
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
