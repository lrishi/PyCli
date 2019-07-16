

def virtualmethod(func):
    def wrapper():
        raise NotImplementedError(
        "Invocation of virtual function [%s] is not permitted" %
        func.__name__)