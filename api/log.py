import os
import logging
from enum import Enum
from datetime import datetime


class Log:

    __instance = None
    __logger = logging.getLogger("PyCli.%s"%datetime.now())

    def log(self, level, object):
        caller = Log.__logger.findCaller()
        #fpath = "%s/%s" % (os.path.split(os.path.split(caller[0])[0])[1], os.path.basename(caller[0]))
        pfmt = "%s %-5s %s:%s %s() =>"%(datetime.now(), logging.getLevelName(level),
                caller[0], caller[1], caller[2])
        Log.__logger.log(level, "%s %s" % (pfmt, object))

    @staticmethod
    def get_instance():
        if Log.__instance is None:
            """
            "" This implementation doesn't depend on the lock for
            "" returning the instance in steady state. This code path
            "" is exercised only during the state creation.
            ""s
            """
            import threading
            with threading.Lock():
                """
                "" Check again, an instance might have become available
                "" while we were waiting. Say thanks to fellow thread.
                ""
                """
                if Log.__instance is None:
                    Log.__instance = Log()
                    lg = Log.__logger
                    lg.setLevel(logging.DEBUG)
                    fh = logging.FileHandler("/var/log/pycli/%s.log"
                                             %
                                             lg.name.replace(" ", "-").replace(":", "."))
                    fh.setFormatter(
                        logging.Formatter(
                            '%(message)s'
                        )
                    )
                    lg.addHandler(fh)
                    Log.d("Logging is initialized")
        return Log.__instance

    @staticmethod
    def set_level(self, level):
        if (level in range(logging.NOTSET, logging.CRITICAL)):
            self.__logger.setLevel(level)

    @staticmethod
    def d(*args, **kwargs):
        level = logging.DEBUG
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def i(*args, **kwargs):
        level = logging.INFO
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def w(*args, **kwargs):
        level = logging.WARNING
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def e(*args, **kwargs):
        level = logging.ERROR
        Log.get_instance().log(level, *args, **kwargs)

    @staticmethod
    def c(*args, **kwargs):
        level = logging.CRITICAL
        Log.get_instance().log(level, *args, **kwargs)

