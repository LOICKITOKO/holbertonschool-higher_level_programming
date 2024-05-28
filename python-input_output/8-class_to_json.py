#!/usr/bin/python
'''
    function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an objec
'''


def class_to_json(obj):
    '''Return the dictionary description with simple data structures for JSON serialization of an object'''
    return obj.__dict__
