from PyCli.api.exceptions import *
from PyCli.api.node import PyCliNode

class PyCliTree(object):
    
    __tree_root = {"this": None, "children": {}}
    
    def __init__(self):
        pass
        
    def __str__(self):
        retstr = "+--[ROOT>\n"
        indent = "   "        
        return retstr + self.__tree_str(self.__tree_root["children"], indent)
    
    def __tree_str(self, root, indent):
        retstr = ""
        for child in root.keys():
            retstr += (indent + "+--[" + child + "%s>\n"%("\u2190\u2190" if (root[child]["this"] and root[child]["this"].data_execute is not None) else ">"))
            retstr += self.__tree_str(root[child]["children"], indent + "   ")
        return retstr
    
    def find_executable(self, tokens, nois):
        cp = self.__tree_root["children"]
        cpt = self.__tree_root["this"]
        flag = nois
        for token in tokens:
            if token not in cp.keys():
                return None
            if flag is True:
                flag = False
                if cp[token]["this"].data_nois is False:
                    return None
            cpt = cp[token]["this"]
            cp = cp[token]["children"]
        return (cpt.data_execute, cpt.data_type, nois)
        
    def find_all_help(self, tokens, nois=False):
        cp = self.__tree_root["children"]
        flag = nois
        for token in tokens:
            if token not in cp.keys():
                return None
            if flag is True:
                flag = False
                if nois is True and cp[token]["this"].data_nois == False:
                    return None
            cp = cp[token]["children"]
        retlist = []
        for lp in cp.keys():
            if flag is True:
                if cp[lp]["this"].data_nois is False:
                    continue
            #print(lp, cp[lp], cp[lp]["this"].data_name)
            retlist.append({"name": lp, "help": cp[lp]["this"].data_help})
        return retlist
            
    def _attach_node(self, node):
        lp = node.data_link
        if len(lp) is 1 and lp[0] is '':
            if node.data_name not in self.__tree_root:
                self.__tree_root["children"][node.data_name] = {}
                self.__tree_root["children"][node.data_name]["children"] = {}
            self.__tree_root["children"][node.data_name]["this"] = node
        else:
            cp = self.__tree_root
            for lp in node.data_link:
                if lp not in cp["children"]:
                    cp["children"][lp] = {}
                    cp["children"][lp]["this"] = None
                    cp["children"][lp]["children"] = {}
                cp = cp["children"][lp]
            cp["children"][node.data_name] = {}
            cp["children"][node.data_name]["children"] = {}
            cp["children"][node.data_name]["this"] = node
                    
    def attach(self, nodes):
        if type(nodes) is not list:
            raise PyCliTypeError("nodes", list)
            
        for node in nodes:
            self._attach_node(node)
            

if __name__ == "__main__":
    from PyCli.api.parser import PyCliParser
    from PyCli.api.node import PyCliNodeBuilder
    pcp = PyCliParser(".")
    nodes = pcp.parse(pcp.find())
    tree = PyCliTree()
    tree.attach(nodes)
    print(tree)