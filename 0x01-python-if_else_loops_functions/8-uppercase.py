#!/usr/bin/python3

def uppercase(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)
::w
def uppercase(string):
    string_new = ""
