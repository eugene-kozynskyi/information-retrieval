#!/c/Users/egood/AppData/Local/Programs/Python/Python35/python

import xml.etree.ElementTree as ET
import io
import os.path as path
import os

def resolve_namespace(xmlroot_name) -> str:
    if xmlroot_name[0] == "{":
        uri, tag = xmlroot_name[1:].split("}")
        return uri
    else:
        return ''

def process_word(word) -> str:
    return ''.join(e for e in word.lower() if e.isalpha())

def iter_tokens(filepath):
    with io.open(filepath, 'r', encoding='utf8') as file:
        root = ET.parse(file).getroot()
        namespace = resolve_namespace(root.tag)
        for element in root.iterfind('.//{%s}p' % namespace):
            for line in element.itertext():
                for word in line.split():
                    token = process_word(word)
                    if len(token) > 0:
                        yield token

def get_fb2(dir) -> list:
    return [f for f in map(lambda p: path.join(dir, p), os.listdir(dir))
            if path.isfile(f) and f.endswith('.fb2')]


def create_dict(dir):
    for filepath in get_fb2(dir):
        for word in iter_tokens(filepath):
            print('{0} {1}'.format(word, path.basename(filepath))),

def main():
    create_dict('texts');

if __name__ == '__main__':
    main();