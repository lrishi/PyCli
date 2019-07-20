import os

from PyCli.api.node import PyCliNodeBuilder
        

class PyCliParser(object):
    
    __extensions = (".pycli")
    __search_path = "."
    __nodes = []
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
        for t in self.__tree:
            self.__nodes += list(map(PyCliNodeBuilder.get, t))
        return self.__nodes
        
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