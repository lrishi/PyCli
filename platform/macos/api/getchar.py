""" MacOS specific getchar implementation """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


from PyCli.api.getchar import GetChar as IGetChar


class GetCharMacOS(IGetChar):
    """ MacOS specific GetChar implementation """

    def __str__(self):
        return str(super()) + "=>" + self.__class__.__name__

    def stdin(self, count=1):
        """ Get <count> chars from stdin """
        raise NotImplementedError("MacOS is not supported yet!")
