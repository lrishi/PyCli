import logging
from enum import Enum
from datetime import datetime


class Log:
    
    class Level(Enum):
        NOLOG = 0
        CRITICAL = 1
        ERROR = 2
        WARNING = 3 
        INFO = 4
        DEBUG = 5
        VERBOSE = 6
    
    
    __instance = None
    __logger = logging.getLogger("PyCli.%s"%datetime.now())
    
    def log(self, level, object):
        print(object)
    
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
                    Log.__logger.setLevel(logging.DEBUG)
                    Log.v("Logging is initialized")
        return Log.__instance
    
    @staticmethod
    def set_level(self, level):
        if (level in range(Log.Level.NOLOG, Log.Level.VERBOSE + 1)):
            self.__logger.setLevel(level)
            
    @staticmethod
    def v(*args, **kwargs):
        level = Log.Level.VERBOSE
        Log.get_instance().log(level, *args, **kwargs)
    
    @staticmethod
    def d(*args, **kwargs):
        level = Log.Level.DEBUG
        Log.get_instance().log(level, *args, **kwargs)
    
    @staticmethod
    def i(*args, **kwargs):
        level = Log.Level.INFO
        Log.get_instance().log(level, args, kwargs)
    
    @staticmethod
    def e(*args, **kwargs):
        level = Log.Level.ERROR
        Log.get_instance().log(level, args, kwargs)
    
    @staticmethod
    def c(*args, **kwargs):
        level = Log.Level.CRITICAL
        Log.get_instance().log(level, args, kwargs)
        