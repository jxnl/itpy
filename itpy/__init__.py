# -*- coding: utf-8 -*-

"""
itpy
~~~~

Built on the back of itertools, `itpy` allows easy list processing through chaining methods.
Everything is a lazy evaluated generating function so nothing happens until you call a method
with side effects. This allows for a fast memory effecient 'keep what you need' way of processing
large ammounts of data!

"""
from __future__ import print_function

from copy import deepcopy

from decorators import iter_wraps, term_wraps
from lambdas import keyf, valuef, identity

import transforms
import summary
import sketch


class Itpy(object):

    VALUE = None

    def __init__(self, iterable=None):
        self._iter = iterable

    @property
    def _(self):
        return list(self)

    @iter_wraps(transforms.map_)
    def map(self, function):
        return Itpy()

    @iter_wraps(transforms.flatmap)
    def flatmap(self, function_to_list):
        return Itpy()

    @iter_wraps(transforms.filter_)
    def filter(self, predicate):
        return Itpy()

    @iter_wraps(transforms.filterfalse)
    def filterfalse(self, predicate):
        return Itpy()

    @iter_wraps(transforms.reduceby)
    def reduceby(self, reducer, key=keyf, value=valuef):
        return Itpy()

    @iter_wraps(transforms.groupby)
    def groupby(self, key=identity, value=identity):
        return Itpy()

    @iter_wraps(transforms.takewhile)
    def takewhile(self, predicate):
        return Itpy()

    @iter_wraps(transforms.dropwhile)
    def dropwhile(self, predicate):
        return Itpy()

    @iter_wraps(transforms.union)
    def union(self, *iterable):
        return Itpy()

    @iter_wraps(transforms.top)
    def top(self, max_size=1, key=None):
        return Itpy()

    @iter_wraps(transforms.take)
    def take(self, max):
        return Itpy()

    @iter_wraps(transforms.sort)
    def sort(self, cmp=None, key=None, reverse=False):
        return Itpy()

    @iter_wraps(transforms.slice_)
    def slice(self, *args):
        return Itpy()

    @iter_wraps(transforms.sample_without_replacement)
    def sample_without_replacement(self, max_size):
        return Itpy()

    @iter_wraps(transforms.distinct)
    def distinct(self):
        return Itpy()

    @term_wraps(summary.reduce_)
    def reduce(self, reducer):
        return Itpy.VALUE

    def __iter__(self):
        for item in self._iter:
            yield item
