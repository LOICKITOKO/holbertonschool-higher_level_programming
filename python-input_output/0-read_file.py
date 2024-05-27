#!/usr/bin/python3


def read_file(filename=""):
    '''
        Open the file in read mode with UTF-8 encoding
        The with statement ensures that the file is properly closed after use
    '''

    with open(filename, "r", encoding="utf-8") as file:
            #Read the entire content of the file and store it in the variable content 
            content = file.read()
            # Print the content of the file to the standard output
            print(content)

