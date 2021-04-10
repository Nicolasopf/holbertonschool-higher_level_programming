#!/usr/bin/python3
""" Get the header value"""
import requests
from sys import argv


if __name__ == "__main__":
    info = requests.get("https://api.github.com/repos/" + argv[1] + "/" +
                        argv[2] + "/commits")

    text = info.json()
    try:
        for i in range(10):
            print('{}: {}'.format(text[i].get('sha'), text[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass
