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
    
    
    __instance = Log()
    __logger = logging.getLogger("PyCli.%d"%datetime.now())
    
    def log(self, object):
        print(object)
    
    def get_instance(self):
        return Log.__instance    
    
    @staticmethod
    def set_level(self, level):
        if (level in range(Log.Level.NOLOG, Log.Level.VERBOSE + 1)):
            
            
    @staticmethod
    def v(*args, **kwargs):
        level = Log.Level.VERBOSE
        Log.get_instance().log(level, args, kwargs)
    
    @staticmethod
    def d(*args, **kwargs):
        level = Log.Level.DEBUG
        Log.get_instance().log(level, args, kwargs)
    
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
        