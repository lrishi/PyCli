""" PyCli specific exceptions """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


class PyCliInvalidArgument(Exception):
    """ Invalid argument exception """

    def __init__(self, arg, arg_t):
        super(PyCliInvalidArgument, self).__init__(
            "%s must be of type %s" % (
                str(arg), str(arg_t)
            )
        )


class PyCliTypeError(Exception):
    """ Expected variable type mismatch """

    def __init__(self, arg, arg_t):
        super(PyCliTypeError, self).__init__(
            "%s should be of type %s" % (
                str(arg), str(arg_t)
            )
        )


class PyCliValueError(Exception):
    """ Invalid value in a variable """

    def __init__(self, arg):
        super(PyCliValueError, self).__init__(str(arg))


class PyCliUnsupportedOS(Exception):
    """ Unsupported operating system for PyCli """

    def __init__(self, arg):
        super(PyCliUnsupportedOS, self).__init__(
            "Unsupported operating system => [%s]" % (
                str(arg)
            )
        )
