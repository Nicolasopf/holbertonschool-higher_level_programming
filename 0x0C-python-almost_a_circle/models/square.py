#!/usr/bin/python3
""" class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square is expected to print a square.
    I hope reach the goal.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        dic = ['id', 'size', 'x', 'y']
        if args and args[0] is not None:
            for i in range(len(args)):
                setattr(self, dic[i], args[i])
        else:
            for k in kwargs:
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
