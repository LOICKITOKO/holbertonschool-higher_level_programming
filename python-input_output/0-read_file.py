#!/usr/bin/python3
'''
    Open the file in read mode with UTF-8 encoding
'''


def read_file(filename=""):
    '''read mode with UTF-8 encoding'''
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
