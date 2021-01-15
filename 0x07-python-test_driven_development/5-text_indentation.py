#!/usr/bin/python3
""" Function to do a new line in some cases """


def text_indentation(text):
    """
    Put a new line in puntual cases
    such as . ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for c in text:
        if c in [".", "?", ":"]:
            while i + 1 < len(text) and text[i + 1] == " ":
                text = text[:i + 1] + text[i + 2:]
        else:
            i += 1
    text = text.strip(" ")
    for c in text:
        print(c, end="")
        if c in [".", "?", ":"]:
            print("\n")
