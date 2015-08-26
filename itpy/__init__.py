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

from itpy.decorators import iter_wraps, term_wraps
from itpy.helpers import identity, getitem
import itpy.transforms as transforms
import itpy.summary as summary
import itpy.iio as iio


class Itpy(object):
    VALUE = None

    def __init__(self, iterable=None, itpy=None):
        if iterable:
            self._iter = iter(iterable)
            self._src = type(iterable)
        if itpy:
            self._stack = itpy._stack
            self._src = itpy._src
        else:
            self._stack = []

    """
    Transformations
    ~~~~~~~~~~~~~~~

    These methods provide you with the power to transforms your Itpy datastreams into other data streams through
    chaining methods together.
    """

    @iter_wraps(transforms.map)
    def map(self, function):
        return Itpy(itpy=self)

    @iter_wraps(transforms.flatmap)
    def flatmap(self, function_to_list):
        return Itpy(itpy=self)

    @iter_wraps(transforms.flatten)
    def flatten(self):
        return Itpy(itpy=self)

    @iter_wraps(transforms.fold)
    def fold(self, func, base):
        return Itpy(itpy=self)

    @iter_wraps(transforms.filter)
    def filter(self, predicate):
        return Itpy(itpy=self)

    @iter_wraps(transforms.find)
    def find(self, predictate, n=1):
        return Itpy(itpy=self)

    @iter_wraps(transforms.filterfalse)
    def filterfalse(self, predicate):
        return Itpy(itpy=self)

    @iter_wraps(transforms.sort)
    def sort(self, cmp=None, key=None, reverse=False):
        return Itpy(itpy=self)

    @iter_wraps(transforms.reduceby)
    def reduceby(self, reducer, key=getitem(0), value=getitem(1)):
        return Itpy(itpy=self)

    @iter_wraps(transforms.groupby)
    def groupby(self, keyfunc=identity, value=identity):
        return Itpy(itpy=self)

    @iter_wraps(transforms.grouped)
    def grouped(self, n):
        return Itpy(itpy=self)

    @iter_wraps(transforms.grouped)
    def batch(self, n):
        return Itpy(itpy=self)

    @iter_wraps(transforms.union)
    def union(self, *iterable):
        return Itpy(itpy=self)

    @iter_wraps(transforms.top)
    def top(self, max_size=1, key=None):
        return Itpy(itpy=self)

    @iter_wraps(transforms.takewhile)
    def takewhile(self, predicate):
        return Itpy(itpy=self)

    @iter_wraps(transforms.drop)
    def drop(self, n):
        return Itpy(itpy=self)

    @iter_wraps(transforms.dropwhile)
    def dropwhile(self, predicate):
        return Itpy(itpy=self)

    @iter_wraps(transforms.take)
    def take(self, max):
        return Itpy(itpy=self)

    @iter_wraps(transforms.slice)
    def slice(self, *args):
        return Itpy(itpy=self)

    @iter_wraps(transforms.distinct)
    def distinct(self):
        return Itpy(itpy=self)

    @iter_wraps(transforms.intercept)
    def intercept(self, function):
        return Itpy(itpy=self)

    @term_wraps(summary.frequency)
    def frequency(self):
        return Itpy.VALUE

    @term_wraps(summary.mean)
    def mean(self):
        return Itpy.VALUE

    @term_wraps(summary.online_variance)
    def variance(self):
        return Itpy.VALUE

    @term_wraps(summary.for_each)
    def for_each(self, function):
        return Itpy.VALUE

    @term_wraps(transform.for_all)
    def for_all(self, predicate):
        return Itpy.VALUE

    @term_wraps(summary.reduce)
    def reduce(self, reducer):
        return Itpy.VALUE

    @term_wraps(summary.size)
    def size(self):
        return Itpy.VALUE

    @staticmethod
    @iter_wraps(iio.from_file)
    def from_file(path_to_file, buffer=1):
        return Itpy()

    @staticmethod
    @iter_wraps(iio.from_stdin)
    def from_stdin(self):
        return Itpy()

    @term_wraps(iio.to_stdout)
    def to_stdout(self):
        return Itpy.VALUE

    @term_wraps(iio.to_file)
    def to_file(self, path_to_file):
        return Itpy.VALUE

    """
    Sketching methods
    ~~~~~~~~~~~~~~~~~

    These algorithms have limited memory available to them (much less than the input size) and also limited
    processing time per item. These constraints may mean that an algorithm produces an approximate answer
    based on a summary or "sketch" of the data stream in memory.

    TODO : HyperLogLog, Count-min

    """

    # @term_wraps(sketch.count_distinct_approx)
    # def count_distinct_approx(self, init_cap=200, err_rate=0.001):
    # return Itpy.VALUE

    # @term_wraps(sketch.to_bloomfilter)
    # def to_bloomfilter(self, init_cap=200, err_rate=0.001):
    # return Itpy.VALUE


    @property
    def _(self):  # Collect the elements of the iter into a list
        return list(self)

    def __repr__(self):
        return "Itpy({}).{}".format(self._src, ".".join(self._stack))

    def __radd__(self, other):
        if other.__iter__:
            return self.union(iter(other))

    def __iter__(self):
        for item in self._iter:
            yield item

    def __len__(self):
        return -1

    def next(self):
        return self._iter.next()
