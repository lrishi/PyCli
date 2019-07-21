""" Linux implementation of GetChar """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


import tty
import sys
import termios
from PyCli.api.getchar import GetChar as IGetChar


class GetCharLinux(IGetChar):
    """ Linux implementation of GetChar """

    def __str__(self):
        return str(super()) + "=>" + self.__class__.__name__

    def stdin(self, count=1):
        """ Get <count> chars from stdin """
        fdesc = sys.stdin.fileno()
        presets = termios.tcgetattr(fdesc)
        retchr = ""

        try:
            tty.setraw(sys.stdin.fileno())
            retchr = sys.stdin.read(count)
        finally:
            termios.tcsetattr(fdesc, termios.TCSADRAIN, presets)

        return retchr
