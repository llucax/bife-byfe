# vim: set expandtab tabstop=4 shiftwidth=4:

import os

class HIT:
    """Hooks vs IT template engine."""
    root     = '.'
    use_path = False
    group    = ''
    postfix  = '.tpl.html'

    def __init__(self, root = root, postfix = postfix, use_path = use_path, group = group):
        """Constructor."""
        self.root     = root
        self.use_path = use_path
        self.postfix  = postfix
        self.group    = []
        self.cache    = {}
        self.buffer   = {}
        self.group.append(group)

    def parse(self, name, vars = {}, **more_vars):
        """Parses a block of code."""
        cache_key = self.group[len(self.group)-1] + os.sep + name + self.postfix
        filename = self.root + os.sep + cache_key
        if not self.cache.has_key(cache_key):
            self.cache[cache_key] = file(filename).read()
        out = self.cache[cache_key]
        for key, val in vars.items():
            out = out.replace('{' + key + '}', val)
        for key, val in more_vars.items():
            out = out.replace('{' + key + '}', val)
        return out

    def parseBuffered(self, name, vars = {}, **more_vars):
        """Parses a block of code leaving the result in a temporary buffer."""
        self.buffer[self.group + os.sep + name] += self.parse(name, vars);

    def get_buffer(name):
        """Gets a parsed buffer."""
        return self.buffer[self.group + os.sep + name]

    def pop_buffer(name):
        """Pops a parsed buffer."""
        buff = self.buffer[self.group + os.sep + name]
        del self.buffer[self.group + os.sep + name]
        return buff

    def push_group(group = ''):
        """Pushes a group to work on."""
        self.group.append(group)

    def pop_group():
        """Pops the last group worked on."""
        return self.group.pop()

