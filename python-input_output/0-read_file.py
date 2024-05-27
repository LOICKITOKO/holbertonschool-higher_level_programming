#!/usr/bin/python3
'''
    Open the file in read mode with UTF-8 encoding
'''


def read_file(filename=""):
    '''read mode with UTF-8 encoding'''
    with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
