#!/usr/bin/env python
# vim: set et ts=4 sw=4:

from xml.sax         import saxutils, make_parser
from xml.sax.handler import feature_namespaces
from sys             import argv

class Parser(saxutils.DefaultHandler):
    def __init__(self):
        self.level  = 0
        self.parser = make_parser()
        self.parser.setFeature(feature_namespaces, 0)
        self.parser.setContentHandler(self)

    def startElement(self, name, attrs):
        print self.level * '  ', 'Inicio:', name
        self.level += 1
        for key, val in attrs.items():
            print self.level * '  ', key, '=', val

    def endElement(self, name):
        self.level -= 1
        print self.level * '  ', 'Fin:', name

    def characters(self, data):
        print self.level * '  ', 'Datos:', data

    def parse(self, file):
        self.parser.parse(file)

if __name__ == '__main__':
    Parser().parse(argv[1])
