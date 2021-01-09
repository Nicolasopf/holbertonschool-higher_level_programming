#!/usr/bin/python3
""" Function to do a new line in some cases """


def text_indentation(text):
    """
    Put a new line in puntual cases
    such as . ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    tex = text.strip(" ")
    for i in range(len(tex)):
        if tex[i - 1] in [".", "?", ":"] and tex[i] == " ":
            continue
        print(tex[i], end='')
        if tex[i] in [".", "?", ":"]:
            print()
            print()
