#!/bin/bash
# Makes the server respond with a message "You got me!"
curl -X PUT 0:5000/catch_me -L -d "user_id=98" -H "Origin: HolbertonSchool"
