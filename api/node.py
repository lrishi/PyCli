from PyCli.api.exceptions import PyCliValueError


class PyCliNode(object):
    
    data_name = None
    data_help = None
    data_link = None
    data_type = None
    
    data_nois = False
    data_execute = None
    
    def __str__(self):
        return  ("Name: %s, Linkpoint: %s, Type: %s, No: %s [%s]" %
                    (
                        self.data_name,
                        self.data_link,
                        self.data_type,
                        self.data_nois,
                        super().__str__()
                    )   
                )
        
    def __init__(self, name, help, link, type=None, nois=False, execute=None):
        self.data_name = name
        self.data_help = help
        self.data_link = link
        self.data_type = type
        
        self.data_nois = nois
        self.data_execute = execute
        
    def attach(self, node):
        if type(node) is not PyCliNode:
            raise PyCliTypeError("node", PyCliNode)
        
        if key in self._children:
            raise PyCliValueError("%s CLI key is duplicated, exists at %s" % (key, self._children[key]))
        
        self._children[key] = node



class PyCliNodeBuilder(object):
    
    mandatory = {}
    optional = {}
    
    def __init__(self):
        self.mandatory = {
            "name": None,
            "help": None,
            "link": None,
        }
        self.optional = {
            "type": None,
            "nois": False,
            "execute": None
        }
        
    def _get(self):
        return PyCliNode(  
                    link=self.mandatory["link"],
                    name=self.mandatory["name"],
                    help=self.mandatory["help"],
                    type=self.optional["type"],
                    nois=self.optional["nois"],
                    execute=self.optional["execute"]
                )
    
    @staticmethod
    def get(dictionary):
        # Parse mandatory args
        pcnb = PyCliNodeBuilder()
        for key in pcnb.mandatory.keys():
            pcnb.mandatory[key] = dictionary[key]
        
        for key in pcnb.optional.keys():
            if key in dictionary:
                pcnb.optional[key] = dictionary[key]
        
        return pcnb._get()        
