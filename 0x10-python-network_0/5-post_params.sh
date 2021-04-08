#!/usr/bin/env bash
# Print body of response and send info in a post request
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
