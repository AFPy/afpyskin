#
from deliverance import rules
from pyquery import PyQuery as pq

class PyQuery(rules.AbstractAction):
    """PyQuery rule for deliverance"""
    name = 'pyquery'
    def __init__(self, source_location, callback=None):
        self.source_location = source_location
        self.callback = callback

    def apply(self, content_doc, theme_doc, resource_fetcher, log):
        """apply the rule"""
        self.callback(pq([content_doc]), pq([theme_doc]), resource_fetcher, log)

    @classmethod
    def from_xml(cls, tag, source_location):
        """Parses and instantiates the class from an element"""
        use = tag.attrib['use']
        modname, funcname = use.split(':')
        mod = __import__(modname, globals(), locals(), [''])
        callback = getattr(mod, funcname)
        return cls(source_location, callback)

# register the new rule
rules._actions['pyquery'] = PyQuery

def afpy_proxy():
    import deliverance.proxycommand
    deliverance.proxycommand.main()
