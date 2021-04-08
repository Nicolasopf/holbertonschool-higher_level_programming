#!/usr/bin/env bash
# Prints the body size
curl "$1" | grep "Content-Length:" | cut -d " " -f 2
