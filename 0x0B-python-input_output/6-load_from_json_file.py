#!/usr/bin/python3
""" creates an Object from a “JSON file” """


def load_from_json_file(filename):
    """ heyyyyyyy more no needed comments """
    with open(filename) as f:
        import json
        return json.load(f)
