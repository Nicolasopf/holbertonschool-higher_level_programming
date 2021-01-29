#!/usr/bin/python3
"""
Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)
"""
import json
import csv


class Base:
    """ This class will be the “base” of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        """  def init  """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert to json string """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to a file """
        fille = "{}.json".format(cls.__name__)
        with open(fille, 'w', encoding="UTF-8") as file:
            ll = []
            if list_objs is None:
                file.write(str(ll))
            else:
                for i in list_objs:
                    ll.append(cls.to_dictionary(i))
                ll = Base.to_json_string(ll)
                file.write(str(ll))

    @staticmethod
    def from_json_string(json_string):
        """ From json to string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create cls """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load from a file """
        ll = []
        try:
            fille = "{}.json".format(cls.__name__)
            with open(fille) as file:
                for d in cls.from_json_string(file.read()):
                    ll.append(cls.create(**d))
                return ll
        except Exception:
            return ll

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to a file in csv """
        fille = "{}.csv".format(cls.__name__)
        ll = [d.to_dictionary() for d in list_objs]
        with open(fille, 'w', encoding="UTF-8") as file:
            file.write(cls.to_json_string(ll))

    @classmethod
    def load_from_file_csv(cls):
        """ Load from a file csv """
        fille = "{}.csv".format(cls.__name__)
        list_objs = []
        try:
            with open(fille, encoding="UTF-8") as file:
                ll = cls.from_json_string(file.read())
                for d in ll:
                    list_objs.append(cls.create(**d))
                return list_objs
        except Exception:
            return list_objs
