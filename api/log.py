""" Logging wrapper for PyCli """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


import logging
from datetime import datetime


class Log():
    """ Direct access log class (android style) """

    __instance = None
    __logger = logging.getLogger("PyCli.%s"%datetime.now())

    def set_log_level(self, level):
        """ Set level """
        self.__logger.setLevel(level)

    def log(self, level, obj_to_log):
        """ Single point for final logging """
        caller = self.__logger.findCaller()
        pfmt = "%s %-5s %s:%s %s() =>" % (datetime.now(),
                                          logging.getLevelName(level),
                                          caller[0], caller[1], caller[2])
        self.__logger.log(level, "%s %s", pfmt, obj_to_log)

    @staticmethod
    def get_instance():
        """ Create/get instance """
        if Log.__instance is None:
            # This implementation doesn't depend on the lock for
            # returning the instance in steady state. This code path
            # is exercised only during the state creation.

            import threading
            with threading.Lock():
                # Check again, an instance might have become available
                # while we were waiting. Say thanks to fellow thread.

                if Log.__instance is None:
                    Log.__instance = Log()
                    mlg = Log.__logger
                    mlg.setLevel(logging.DEBUG)
                    mfh = logging.FileHandler("/var/log/pycli/%s.log"
                                              %
                                              mlg.name.replace(" ", "-").replace(":", "."))
                    mfh.setFormatter(
                        logging.Formatter(
                            '%(message)s'
                        )
                    )
                    mlg.addHandler(mfh)
                    Log.d("Logging is initialized")
        return Log.__instance

    @staticmethod
    def set_level(level):
        """ Set logging level """
        if level in range(logging.NOTSET, logging.CRITICAL):
            Log.get_instance().set_log_level(level)


    @staticmethod
    def d(*args, **kwargs):
        """ Log to DEBUG level """
        #pylint: disable=invalid-name
        level = logging.DEBUG
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def i(*args, **kwargs):
        """ Log to INFO level """
        #pylint: disable=invalid-name
        level = logging.INFO
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def w(*args, **kwargs):
        """ Log to WARNING level """
        #pylint: disable=invalid-name
        level = logging.WARNING
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def e(*args, **kwargs):
        """ Log to ERROR level """
        #pylint: disable=invalid-name
        level = logging.ERROR
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def c(*args, **kwargs):
        """ Log to CRITICAL level """
        #pylint: disable=invalid-name
        level = logging.CRITICAL
        Log.get_instance().log(level, *args, **kwargs)
