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

    # transforms
    @iter_wraps(transforms.distinct)
    def distinct(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.intercept)
    def intercept(iterable, function):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.drop)
    def drop(iterable, n):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.dropwhile)
    def dropwhile(iterable, predicate):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.filter)
    def filter(iterable, predicate):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.filterfalse)
    def filterfalse(iterable, predicate):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.find)
    def find(iterable, predicate, n=1):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.flatmap)
    def flatmap(iterable, function_to_list):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.flatten)
    def flatten(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.fold)
    def fold(iterable, func, base):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.grouped)
    def grouped(iterable, n):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.has_definite_size)
    def has_definite_size(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.map)
    def map(iterable, function):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.max)
    def max(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.maxBy)
    def maxBy(iterable, function):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.min)
    def min(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.minBy)
    def minBy(iterable, function):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.partition)
    def partition(iterable, predicate):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.permutations)
    def permutations(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.intersect)
    def intersect(iterable, other):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.slice)
    def slice(iterable, *args):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.size)
    def size(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.sort)
    def sort(iterable, **kwargs):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.top)
    def top(iterable, max_size=1, key=None):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.take)
    def take(iterable, n):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.takewhile)
    def takewhile(iterable, predicate):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.reduceby)
    def reduceby(iterable, reducer, key=getitem(0), value=getitem(1)):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.toArray)
    def toArray(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.toList)
    def toList(iterable):
        return Itpy(itpy=iterable)

    @iter_wraps(transforms.union)
    def union(iterable, *iterables):
        return Itpy(itpy=iterable)

    # summary
    @term_wraps(summary.for_all)
    def for_all(iterable, predicate):
        return Itpy.VALUE

    @term_wraps(summary.groupby)
    def groupby(iterable, keyfunc=identity, value=identity):
        return Itpy.VALUE

    @term_wraps(summary.for_each)
    def for_each(iterable, function):
        return Itpy.VALUE

    @term_wraps(summary.size)
    def size(iterable):
        return Itpy.VALUE

    @term_wraps(summary.reduce)
    def reduce(iterable, reducer):
        return Itpy.VALUE

    @term_wraps(summary.frequency)
    def frequency(iterable):
        return Itpy.VALUE

    @term_wraps(summary.mean)
    def mean(iterable):
        return Itpy.VALUE

    @term_wraps(summary.twopass_variance)
    def twopass_variance(iterable):
        return Itpy.VALUE

    @term_wraps(summary.sample)
    def sample(iterable, max_size):
        return Itpy.VALUE

    @term_wraps(summary.online_variance)
    def variance(iterable):
        return Itpy.VALUE

    # iio
    @iter_wraps(iio.from_file)
    def from_file(path_to_file, buffer=1):
        return Itpy()

    @iter_wraps(iio.from_stdin)
    def from_stdin(self):
        return Itpy()

    # Sketches

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

    def next(self):
        return self._iter.next()
