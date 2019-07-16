from PyCli.lib.abstract import AbstractOS
from PyCli.lib.decorators import virtualmethod
from PyCli.lib.exceptions import 

class GetChar(object):
    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __new__(cls, *args, **kwargs):
        if AbstractOS.is_windows():
            from PyCli.platform.win32.lib.getchar import GetCharWindows
            return object.__new__(GetCharWindows, *args, **kwargs)
        if AbstractOS.is_linux():
            from PyCli.platform.linux.lib.getchar import GetCharLinux
            return object.__new__(GetCharLinux, *args, **kwargs)
        if AbstractOS.is_macos():
            from PyCli.platform.macos.lib.getchar import GetCharMacOS
            return object.__new__(GetCharMacOS, *args, **kwargs)
        raise PyCliUnsupportedOS(AbstractOS.get_os_name())

    @virtualmethod
    def stdin(self, count=1):
        pass

"""
catch = GetChar()

print(catch.stdin())
"""
