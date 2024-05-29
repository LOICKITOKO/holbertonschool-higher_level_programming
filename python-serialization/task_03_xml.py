#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''Serialize a dictionary to an XML file'''
    root = ET.Element("data")
    for key, value in dictionary.items():
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    '''Deserialize an XML file to a dictionary'''
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        _dict = {}
        for element in root:
            _dict[element.tag] = element.text
            return _dict
    except Exception as e:
        print(f"An error occurrend while deserializing from XML: {e}")
        return None
