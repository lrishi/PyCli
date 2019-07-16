"""
"" Copyright (c) 2019, Lovel Rishi (lrishi)
""
""
"" Module:         abstract.py
"" Description:    Define abstractions for platform specific attributes
""
"" Date Created:   14 Jul 2019
"" Author:         Lovel Rishi (lrishi)
""
"""
from sys import platform


class AbstractOS(object):
    """
    "" OS platform needs to be identified to enhance terminal
    "" functionality. A class might be required in future to keep it clean.
    ""
    """

    __is_linux = ((platform == "linux") or
                  (platform == "linux2") or
                  (platform == "linux3"))
    __is_macos = (platform == "darwin")
    __is_windows = (platform == "win32")

    @staticmethod
    def is_windows():
        """
        "" Return true if os is Windows
        ""
        """
        return AbstractOS.__is_windows

    @staticmethod
    def is_linux():
        """
        "" Return true if os is Linux
        ""
        """
        return AbstractOS.__is_linux

    @staticmethod
    def is_macos():
        """
        "" Return true if os is MacOS
        ""
        """
        return AbstractOS.__is_macos
        
    @staticmethod
    def get_os_name():
        """
        "" Return current os name
        ""
        """
        return (str(platform) if platform is not "" else "Unknown")
