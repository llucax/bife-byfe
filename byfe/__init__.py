# vim: set expandtab tabstop=4 shiftwidth=4:

class widget:
    """Base widget class."""

    def __init__(self, attrs = None):
        if attrs is None:
            attrs = {}
        self.attrs = attrs

    def __repr__(self):
        return 'widget(attrs=' + str(self.attrs) + ')'

    def render(self, userdata = None):
        return str(self)


class container(widget):
    """Base container widget class."""

    def __init__(self, attrs = None, content = None):
        widget.__init__(self, attrs)
        self.content = []
        if content:
            self.content.append(content)

    def __repr__(self):
        return 'container(attrs=' + str(self.attrs) + ', content=' \
            + str(self.content) + ')'

    def __len__(self):
        return len(self.content)

    def __getitem__(self, item):
        return self.content[item]

    def __setitem__(self, item, value):
        self.content[item] = value

    def __delitem__(self, item):
        del self.content[item]

    def __contains__(self, item):
        return item in self.content

    def __iter__(self):
        for i in self.content: yield i

    def append(self, content):
        self.content.append(content)

    def extend(self, content):
        self.content.extend(content)

    def renderContent(self, userdata = None):
        out = ''
        for content in self.content:
            if isinstance(content, widget):
                out += content.render(userdata)
            else:
                out += str(content);
        return out;


class fallback(container):
    """Fallback widget to use when no specific widget is implemented."""

    def __init__(self, name, attrs = None, content = None):
        container.__init__(self, attrs, content)
        self.name = name

    def __repr__(self):
        return 'fallback(name=\'' + str(self.name) + '\', attrs=' \
            + str(self.attrs) + ', content=' + str(self.content) + ')'

