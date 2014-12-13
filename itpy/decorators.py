# -*- coding: utf-8 -*-

"""
itpy.utils
~~~~~~~~~~

This module contains the decorators bridge the syntax with the computation. It will also carry over any documentation
that the computational. It is up to the programmer to make sure that the signitures of each align...
"""

from functools import wraps


# noinspection PyPep8Naming
class iter_wraps(object):
    """
    This decorator will highjack any function that returns an Iter() and populates it's insides with the resulting
    generator defined in the argument of the decorator's constructor.

    @iter_wraps(itertools.map)
    def map(self, f):
        return Iter()

    """

    def __init__(self, transformation):
        self.transform = transformation

    def __call__(self, victim):

        @wraps(victim)
        def wrapped(*args, **kwargs):
            it = victim(*args, **kwargs)
            it._iter = self.transform(*args, **kwargs)
            return it

        if self.transform.__doc__:
            wrapped.__name__ = self.transform.__name__
            wrapped.__doc__ = self.transform.__doc__

        return wrapped


# noinspection PyPep8Naming
class term_wraps(object):
    """
    This decorator will high-jack any function that does not return an Iter() and populates it with the resulting
    valued defined by as the argument of the decorator's constructor.

    @term_wraps(itpy.transform.collect)
    def collect(self, f):
        return Itpy.VALUE

    """

    def __init__(self, transformation):
        self.transform = transformation

    def __call__(self, victim):

        @wraps(victim)
        def wrapped(*args, **kwargs):
            return self.transform(*args, **kwargs)

        if self.transform.__doc__:
            wrapped.__name__ = self.transform.__name__
            wrapped.__doc__ = self.transform.__doc__

        return wrapped