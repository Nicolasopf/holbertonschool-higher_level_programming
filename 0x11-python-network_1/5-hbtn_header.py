#!/usr/bin/python3
""" Get the header value"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers['X-Request-Id'])
