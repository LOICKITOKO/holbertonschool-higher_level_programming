#!/usr/bin/python3
'''
    function that appends a string at the end of a text file
'''


def append_write(filename="", text=""):
    '''open the file in append mode'''
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
        return count
