import os

from PyCli.api.tree import PyCliNode

class PyCliNodeBuilder(object):
    
    mandatory = {
        "name": None,
        "help": None,
        "link": None,
    }
    
    optional = {
        "type": None,
        "capture": None,
        "execute": None
    }
    
    def _get(self):
        return PyCliNode(  
                    link=self.mandatory["link"],
                    name=self.mandatory["name"],
                    help=self.mandatory["help"],
                    type=self.optional["type"],
                    capture=self.optional["capture"],
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
        
        

class PyCliParser(object):
    
    __extensions = (".pycli")
    __search_path = "."
    __tree = []
    
    def __init__(self, search_path):
        self.__search_path = search_path
    
    def _parse(self, fname):
        with open(fname) as f:
            out = f.read()
            bp = eval(out)
            self.__tree.append(bp)
        
    def parse(self, files):
        for fn in files:
            self._parse(fn)
        return self.__tree
        
    def find(self):
        file_names = [fn for fn in os.listdir(self.__search_path) if fn.endswith(self.__extensions)]
        return (file_names)


if __name__ == "__main__":
    pcp = PyCliParser(".")
    dtree = pcp.parse(pcp.find())
    print(dtree)
    for d in dtree:
        for m in d:
            node = PyCliNodeBuilder.get(m)
            print(node)
            
    
