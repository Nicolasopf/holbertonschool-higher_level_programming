#!/usr/bin/python3
""" Get the header value"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info().get("X-Request-Id"))
