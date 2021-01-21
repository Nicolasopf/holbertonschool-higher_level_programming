#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation """


def save_to_json_file(my_obj, filename):
    """ Same as above """
    with open(filename, encoding="UTF-8", mode="w+") as f:
        import json
        f.write(json.dumps(my_obj))
