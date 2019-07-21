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

    def auto_complete(self, tokens):
        """ Return complete CLI command from short commands """
        cpt = self.__tree_root["children"]
        curr_cli = ""
        matched = False
        nois = False
        flag = True
        if not tokens:
            return curr_cli
        if tokens[0] in ("no"):
            curr_cli += " no"
            nois = True
            tokens.pop(0)

        for token in tokens:
            if matched is True:
                curr_cli += " %s" % token
                continue
            ntkns = [key for key in cpt.keys() if key.startswith(token)]
            if not ntkns or len(ntkns) > 1:
                matched = True
                curr_cli += " %s" % token
                continue
            if nois is True and flag is True and cpt[ntkns[0]]["this"].data_nois is False:
                matched = True
                curr_cli += " %s" % token
                continue
            flag = False
            curr_cli += " %s" % ntkns[0]
            cpt = cpt[ntkns[0]]["children"]
        if curr_cli != "":
            curr_cli = curr_cli[1:]
        curr_cli += " "
        return curr_cli

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

    def find_all_help(self, tokens, nois=False, regex=False):
        """ Find all helps at given bud/leaf from CLI tokens """
        cpt = self.__tree_root["children"]
        cptt = self.__tree_root["this"]
        flag = nois
        tlen = len(tokens)
        idx = 0
        for token in tokens:
            if token not in cpt.keys():
                if regex is True and idx == tlen - 1:
                    break
                else:
                    return None
            if flag is True:
                flag = False
                if nois is True and not cpt[token]["this"].data_nois:
                    return None
            cptt = cpt[token]["this"]
            cpt = cpt[token]["children"]
            idx += 1
        retlist = []
        for lpt in cpt.keys():
            if regex is True and idx == tlen - 1:
                if not lpt.startswith(tokens[idx]):
                    continue
            if flag is True:
                if cpt[lpt]["this"].data_nois is False:
                    continue
            retlist.append({"name": lpt, "help": cpt[lpt]["this"].data_help})
        if cptt and cptt.data_execute is not None:
            retlist.append({"name": "<cr>", "help": "Press enter to execute CLI"})
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
