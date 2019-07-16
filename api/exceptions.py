"""
"" Copyright (c) 2019 - Lovel Rishi (lrishi)
"" 
"" File:            exceptions.py
"" Description:     PyCli specific custom exception definitions.
""
"" Author:          Lovel Rishi (lrishi)
"" Date Created:    14 Jul 2019
"" 
"""


"""
"" edt:     PyCliInvalidArgument
"" desc:    Invalid arguments passed to a method
""
"""
class PyCliInvalidArgument(Exception):
    def __init__(self, arg, arg_t):
        super().__init__(
            "%s must be of type %s" % (
                str(arg), str(arg_t)
            )
        )

"""
"" edt:     PyCliInvalidArgument
"" desc:    Invalid arguments passed to a method
""
"""
class PyCliTypeError(Exception):
    def __init__(self, arg, arg_t):
        super().__init__(
            "%s should be of type %s" % (
                str(arg), str(arg_t)
            )
        )


class PyCliValueError(Exception):
    def __init__(self, arg):
        super().__init__(str(arg))
        

class PyCliUnsupportedOS(Exception):
    def __init__(self, arg):
        super.__init__(
            "Unsupported operating system: %s" % (
                str(arg)
            )
        )