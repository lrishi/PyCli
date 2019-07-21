""" PyCli Decorators """

__author__ = "Lovel Rishi"
__copyright__ = "Copyright (c) 2019, Lovel Rishi"
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Lovel Rishi"
__email__ = "lovelrishi@outlook.com"
__status__ = "Development"


def virtualmethod(func):
    """ Virtual function decorator """

    #pylint: disable=unused-variable
    def wrapper():
        """ Wrapper for virtual function decorator """
        raise NotImplementedError(
            "Invocation of virtual function [%s] is not permitted" %
            func.__name__)
