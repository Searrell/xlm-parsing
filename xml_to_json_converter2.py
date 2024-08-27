import xml.etree.ElementTree as ET
from collections import OrderedDict
import json


def parse_xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    def traverse(element):
        node = OrderedDict()
        for child in element:
            if len(child):
                node[child.tag] = traverse(child)
            else:
                node[child.tag] = child.text
        return node

    catalog = OrderedDict()
    catalog['book'] = []
    for book in root.findall('book'):
        book_data = traverse(book)
        book_data['id'] = book.attrib['id']  # Include the book id
        catalog['book'].append(book_data)

    return catalog


def write_dict_to_json(data, json_file):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


# Example usage
xml_file = 'books.xml'  # Change this to your XML file name
json_file = 'output2.json'

data = parse_xml_to_dict(xml_file)
write_dict_to_json(data, json_file)
