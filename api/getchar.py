from PyCli.api.abstract import AbstractOS
from PyCli.api.decorators import virtualmethod
from PyCli.api.exceptions import PyCliUnsupportedOS
from PyCli.api.log import Log

class GetChar(object):
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
        pass


def getchar_utest():
    gc = GetChar()
    print("Type q to exit, or anything else for no-op:")
    while True:
        c = gc.stdin()
        print(c)
        if c is 'q':
            print("\nExiting!")
            break


if __name__ == "__main__":
    Log.i("Starting up...")
    getchar_utest()