#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """
from sys import argv

save_file = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

try:
    obj = load_json('add_item.json')
except FileNotFoundError:
    obj = []

for i in argv[1:]:
    obj.append(i)

save_file(obj, filename)
