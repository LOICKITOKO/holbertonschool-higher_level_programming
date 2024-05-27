#!/usr/bin/python3
'''
     Open the file in write mode, creating it if it doesn't exist
'''


def write_file(filename="", text=""):
    '''Write the text to the file'''
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
        return count
