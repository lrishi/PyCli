"""
This module enables CLI tree management.
"""

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"

from PyCli.api.exceptions import PyCliTypeError

class PyCliTree():
    """ CLI Tree provider """
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
            retstr += (indent + "+--[" + child +
                       "%s>\n" % ("\u2190\u2190" if (root[child]["this"] and \
                           root[child]["this"].data_execute is not None) else ">"))
            retstr += self.__tree_str(root[child]["children"], indent + "   ")
        return retstr

    def find_executable(self, tokens, nois):
        """ Find executable leaf/bud from CLI tokens """
        cpt = self.__tree_root["children"]
        cptt = self.__tree_root["this"]
        flag = nois
        for token in tokens:
            if token not in cpt.keys():
                return None
            if flag is True:
                flag = False
                if cpt[token]["this"].data_nois is False:
                    return None
            cptt = cpt[token]["this"]
            cpt = cpt[token]["children"]
        return (cptt.data_execute, cptt.data_type, nois)

    def find_all_help(self, tokens, nois=False):
        """ Find all helps at given bud/leaf from CLI tokens """
        cpt = self.__tree_root["children"]
        cptt = self.__tree_root["this"]
        flag = nois
        for token in tokens:
            if token not in cpt.keys():
                return None
            if flag is True:
                flag = False
                if nois is True and not cpt[token]["this"].data_nois:
                    return None
            cptt = cpt[token]["this"]
            cpt = cpt[token]["children"]
        retlist = []
        for lpt in cpt.keys():
            if flag is True:
                if cpt[lpt]["this"].data_nois is False:
                    continue
            retlist.append({"name": lpt, "help": cpt[lpt]["this"].data_help})
        if cptt.data_execute is not None:
            retlist.append({"name": "<<Execute>>", "help": "Execute CLI"})
        return retlist

    def _attach_node(self, node):
        """ Attach a new node to CLI tree """
        lpt = node.data_link
        if len(lpt) == 1 and lpt[0] == '':
            if node.data_name not in self.__tree_root:
                self.__tree_root["children"][node.data_name] = {}
                self.__tree_root["children"][node.data_name]["children"] = {}
            self.__tree_root["children"][node.data_name]["this"] = node
        else:
            cpt = self.__tree_root
            for lpt in node.data_link:
                if lpt not in cpt["children"]:
                    cpt["children"][lpt] = {}
                    cpt["children"][lpt]["this"] = None
                    cpt["children"][lpt]["children"] = {}
                cpt = cpt["children"][lpt]
            cpt["children"][node.data_name] = {}
            cpt["children"][node.data_name]["children"] = {}
            cpt["children"][node.data_name]["this"] = node

    def attach(self, nodes):
        """ Attach multiple nodes to CLI tree """
        if not isinstance(nodes, list):
            raise PyCliTypeError("nodes", list)

        for node in nodes:
            self._attach_node(node)

    @staticmethod
    def quick_ut():
        """ Quickly test PyCliTree """
        from PyCli.api.parser import PyCliParser
        pcp = PyCliParser(".")
        nodes = pcp.parse(pcp.find())
        tree = PyCliTree()
        tree.attach(nodes)
        print(tree)
