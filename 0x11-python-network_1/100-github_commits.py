#!/usr/bin/python3
""" Get the header value"""
import requests
from sys import argv


if __name__ == "__main__":
    info = requests.get("https://api.github.com/repos/" + argv[1] + "/" +
                        argv[2] + "/commits")
    try:
        text = info.json()
        for dic in text[:10]:
            sha = dic.get('sha')
            commit = dic.get('commit')
            if commit.get('author'.get('name')):
                print(sha + ": " + commit.get('author').get('name'))
            else:
                print(sha ": None")
    except:
        pass
