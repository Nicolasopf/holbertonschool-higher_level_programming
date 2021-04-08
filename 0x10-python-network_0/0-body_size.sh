#!/usr/bin/env bash
# Prints the body size
curl $1 | grep "Content-L" | cut -d " " -f 2
