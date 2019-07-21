""" Bundle of operating system abstractions. """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


from sys import platform


class AbstractOS():
    """
    "" OS platform needs to be identified to enhance terminal
    "" functionality. A class might be required in future to keep it clean.
    ""
    """

    __is_linux = (platform in ("linux", "linux2", "linux3"))
    __is_macos = (platform == "darwin")
    __is_windows = (platform == "win32")

    @staticmethod
    def is_windows():
        """ Return true if os is Windows """
        return AbstractOS.__is_windows

    @staticmethod
    def is_linux():
        """ Return true if os is Linux """
        return AbstractOS.__is_linux

    @staticmethod
    def is_macos():
        """ Return true if os is MacOS """
        return AbstractOS.__is_macos

    @staticmethod
    def get_os_name():
        """ Return current os name """
        return str(platform) if platform != "" else "Unknown"
