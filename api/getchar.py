""" Module to get user input from terminal char by char """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


from PyCli.api.abstract import AbstractOS
from PyCli.api.decorators import virtualmethod
from PyCli.api.exceptions import PyCliUnsupportedOS
from PyCli.api.log import Log


class GetChar():
    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __new__(cls, *args, **kwargs):

        if AbstractOS.is_windows():
            Log.d("Operating system is Windows")
            from PyCli.platform.win32.api.getchar import GetCharWindows as GetCharPlatform
        elif AbstractOS.is_linux():
            Log.d("Operating system is Linux")
            from PyCli.platform.linux.api.getchar import GetCharLinux as GetCharPlatform
        elif AbstractOS.is_macos():
            Log.d("Operating system is MacOS")
            from PyCli.platform.macos.api.getchar import GetCharMacOS as GetCharPlatform
        else:
            Log.d("Operating system is %s" % AbstractOS.get_os_name())

        try:
            return object.__new__(GetCharPlatform, *args, **kwargs)
        except UnboundLocalError:
            raise PyCliUnsupportedOS(AbstractOS.get_os_name())


    @virtualmethod
    def stdin(self, count=1):
        """ Get <count> chars from stdin """

    @staticmethod
    def quick_ut():
        """ Quickly instantiate and test GetChar """
        mgc = GetChar()
        print("Type q to exit, or anything else for no-op:")
        while True:
            char = mgc.stdin()
            print(char)
            if char == 'q':
                print("\nExiting!")
                break
