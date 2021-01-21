#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation """


def save_to_json_file(my_obj, filename):
    import json
    json_rep = json.dumps(my_obj)

    with open(filename, encoding="UTF-8", mode="w+") as f:
        return f.write(json_rep)
