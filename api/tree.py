from PyCli.api.exceptions import *

class PyCliNode(object):
    _children = []
    
    data_name = None
    data_help = None
    data_link = None
    data_type = None
    
    data_capture = None
    data_execute = None
    
    def __str__(self):
        return  ("Name: %s, Linkpoint: %s, Type: %s [%s]" %
                    (
                        self.data_name,
                        self.data_link,
                        self.data_type,
                        super().__str__()
                    )   
                )
        
    def __init__(self, name, help, link, type=None, capture=None, execute=None):
        self.data_name = name
        self.data_help = help
        self.data_link = link
        self.data_type = type
        
        self.data_capture = capture
        self.data_execute = execute
        
    def attach(self, node):
        if type(node) is not PyCliNode:
            raise PyCliTypeError("node", PyCliNode)
        
        if key in self._children:
            raise PyCliValueError("%s CLI key is duplicated, exists at %s" % (key, self._children[key]))
        
        self._children[key] = node