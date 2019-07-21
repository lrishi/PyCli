""" Win32 specific GetChar implementation """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


import msvcrt #pylint: disable=import-error
from PyCli.api.getchar import GetChar as IGetChar


class GetCharWindows(IGetChar):
    """ Win32 specific GetChar implementation """

    def __init__(self):
        # Nothing to do here
        pass

    def stdin(self, count=1):
        """ Get <count> chars from stdin """
        retchr = ""

        for _ in range(0, count):
            retchr += msvcrt.getch()

        return retchr
