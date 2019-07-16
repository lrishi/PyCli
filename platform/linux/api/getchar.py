import tty, sys, termios
from PyCli.api.getchar import GetChar as IGetChar


class GetCharLinux(IGetChar, object):
    def __init__(self):
        pass

    def __str__(self):
        return str(super()) + "=>" + self.__name__

    def stdin(self, count=1):
        fdesc = sys.stdin.fileno()
        presets = termios.tcgetattr(fdesc)
        retchr = ""

        #TODO: Implement exception handling

        try:
            tty.setraw(sys.stdin.fileno())
            retchr = sys.stdin.read(count)
        finally:
            termios.tcsetattr(fdesc, termios.TCSADRAIN, presets)

        return retchr
