#!/bin/bash
# Send a request to URL passed and display only the status code
curl -s -o /dev/null -I -w "%{http_code}" "$1"
