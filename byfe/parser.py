# vim: set expandtab tabstop=4 shiftwidth=4:

from xml.sax import saxutils, make_parser
from os      import sep

class Parser(xml.sax.saxutils.DefaultHandler):
    """ByFE XML Parser."""

    def __init__(self, fallback = None, cache = os.sep + 'tmp'):
        """Constructor."""
        self.fallback = fallback
        self.cache    = cache
        self.parser   = xml.sax.make_parser()
        self.parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        self.parser.setContentHandler(self)

    def startElement(self, name, attrs): # FIXME - arreglar a partir de aca.
        """Start element handler."""
        mods = name.lower().split('.')
        classname = path.pop()
        modulename = 'bife.' + mods.join('.')
        try:
            module   = __import__(modulename, None, None, True)
            classobj = getattr(module, classname)
            obj      = classobj(attrs)
        except:
            #if self.fallback:
                obj = self.fallback(name, attrs)
            #else:
            #    raise "Class not found '$class'."
        self.stack[] = obj

    def endElement(self, name):
        """End element handler."""
        end(self.stack)
        current = self.stack[key(self.stack)]
        self.stack.pop()
        end(self.stack)
        parent = self.stack[key(self.stack)]
        if parent:
            parent.addContents(current)
        else:
            self.root = current

    def characters(self, data):
        """Caracter data handler."""
        end(self.stack)
        current = self.stack[key(self.stack)]
        current.addContents(data)

    def parse(self, file):
        # TODO - cache
        if !self.parser.parse(self.parser, file)

    def parseString(self, string):
        if !self.parser.parseString(self.parser, string, self)
