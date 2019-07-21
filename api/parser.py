""" CLI Configuration file parser implementation """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


import os
from ast import literal_eval
from PyCli.api.node import PyCliNodeBuilder


class PyCliParser():
    """ PyCli configuration file parser class """

    __extensions = (".pycli")
    __search_path = "."
    __nodes = []
    __tree = []

    def __init__(self, search_path):
        self.__search_path = search_path

    def _parse(self, fname):
        """ Parse single file """
        with open(fname) as fdesc:
            out = fdesc.read()
            obp = literal_eval(out)
            self.__tree.append(obp)

    def parse(self, files):
        """ Parse multiple files """
        for fname in files:
            self._parse(fname)
        for tnode in self.__tree:
            self.__nodes += list(map(PyCliNodeBuilder.get, tnode))
        return self.__nodes

    def find(self):
        """ Find all .pycli files in a given directory """
        file_names = [fname for fname in os.listdir(self.__search_path) if
                      fname.endswith(self.__extensions)]
        return file_names

    @staticmethod
    def quick_ut():
        """ Quickly test PyCliParser """
        pcp = PyCliParser(".")
        pdict = pcp.parse(pcp.find())
        print(pdict)
        for mpd in pdict:
            for mpm in mpd:
                node = PyCliNodeBuilder.get(mpm)
                print(node)
