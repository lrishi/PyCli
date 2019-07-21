""" PyCli CLI nodes """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


from PyCli.api.decorators import virtualmethod


class PyCliNode():
    """ PyCli Node class that is passed to PyCliTree """
    data_name = None
    data_help = None
    data_link = None
    data_type = None

    data_nois = False
    data_execute = None

    def __str__(self):
        return  "Name: %s, Linkpoint: %s, Type: %s, No: %s [%s]" % (
            self.data_name,
            self.data_link,
            self.data_type,
            self.data_nois,
            super(PyCliNode, self).__str__()
        )

    def __init__(self, name, _help, link, _type=None, nois=False, execute=None):
        self.data_name = name
        self.data_help = _help
        self.data_link = link
        self.data_type = _type
        self.data_nois = nois
        self.data_execute = execute

    @virtualmethod
    def attach(self):
        """ Not supported """

    @virtualmethod
    def detach(self):
        """ Not supported """


class PyCliNodeBuilder():
    """ Node Builder """
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

    def get_node(self):
        """ Create node """
        return PyCliNode(
            link=self.mandatory["link"],
            name=self.mandatory["name"],
            _help=self.mandatory["help"],
            _type=self.optional["type"],
            nois=self.optional["nois"],
            execute=self.optional["execute"]
        )

    @staticmethod
    def get(dictionary):
        """ Parse mandatory and optional args and get node """
        pcnb = PyCliNodeBuilder()
        for key, value in pcnb.mandatory.items():
            pcnb.mandatory[key] = dictionary[key]

        for key, value in pcnb.optional.items():
            if key in dictionary:
                pcnb.optional[key] = dictionary[key]
            else:
                pcnb.optional[key] = value

        return pcnb.get_node()
