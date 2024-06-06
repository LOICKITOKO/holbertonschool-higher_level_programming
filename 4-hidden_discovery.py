#!/usr/bin/python3

import marshal
import os


def main():
    # Path to the compiled file
    compiled_file_path = '/tmp/hidden_4.pyc'

    # Open the compiled file
    with open(compiled_file_path, 'rb') as f:
        # Skip the header of the .pyc file (16 bytes)
        f.read(16)
        # Load the code object from the file
        code = marshal.load(f)

    # Extract the names defined in the module
    names = [name for name in code.co_names if not name.startswith('__')]

    # Print the names in alphabetical order
    for name in sorted(names):
        print(name)
