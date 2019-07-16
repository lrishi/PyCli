import msvcrt
from PyCli.lib.getchar import GetChar as IGetChar


class GetCharWindows(IGetChar, object):

    def __init__(self):
        # Nothing to do here
        pass

    def stdin(self, count=1):
        retchr = ""

        while i in range(0, count):
            retchr += msvcrt.getch()

        return retchr
