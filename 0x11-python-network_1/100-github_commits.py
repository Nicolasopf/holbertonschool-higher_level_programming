#!/usr/bin/python3
""" This module takes takes a GitHub repository commits history and list the
last 10commits. """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                              sys.argv[1])
    request = requests.get(url)
    coms = request.json()
    try:
        for i in range(10):
            print('{}: {}'.format(coms[i].get('sha'), coms[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass
