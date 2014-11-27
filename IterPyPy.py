# -*- coding: utf-8 -*-

"""
IterPyPY
~~~~~~~~

Built on the back of itertools, <code>Iter</code> allows easy list processing through chaining methods.
Everything acts as a lazy evaluated generating function so nothing happens until you call one
of the methods with side effects.

"""

from copy import deepcopy
from heapq import heapreplace, heapify
from collections import defaultdict

import itertools as it


class Iter(object):
    def __init__(self, iterable):
        self._iter = iterable


    def map(self, function):
        """
        Make an iterator that computes the function using arguments from each of the iterables.

        :rtype : Iter
        :param func, a -> b:
        :return:
        """
        return Iter(it.imap(function, self))

    def flatmap(self, function_to_list):
        """
        Make an interator that returns elements from the lists produced by mapping function_to_list.

        :rtype : Iter
        :param function_to_list, a -> [b...]:
        :return:
        """
        return Iter(it.chain(*self.map(function_to_list)))

    def filter(self, predicate):
        """
        Make an iterator that filters elements from iterable returning only those for which the predicate is True.
        If predicate is None, return the items that are true.

        :rtype : Iter
        :param predicate, a -> bool:
        :return:
        """
        return Iter(it.ifilter(predicate, self))

    def filterfalse(self, predicate):
        """
        Make an iterator that filters elements from iterable returning only those for which the predicate is False.
        If predicate is None, return the items that are false

        :rtype : Iter
        :param predicate, a -> bool:
        :return:
        """
        return Iter(it.ifilterfalse(predicate, self))

    def takewhile(self, predicate):
        """
        Make an iterator that returns elements from the iterable as long as the predicate is true.

        :rtype : Iter
        :param predicate, a -> bool:
        :return:
        """
        return Iter(it.takewhile(predicate, self))

    def dropwhile(self, predicate):
        """
        Make an iterator that drops elements from the iterable as long as the predicate is true

        Note, the iterator does not produce any output until the predicate first becomes false,
        so it may have a lengthy start-up time.

        :rtype : Iter
        :param predicate:
        :return:
        """
        return Iter(it.dropwhile(predicate, self))

    def groupby(self, key=None, value=None):
        """
        Make an iterator that returns consecutive keys and groups from the iterable.
        The key and value is computed each element by keyfunc and valfunc.
        If these functions are not not specified or is None, they default to identity function.

        :rtype : Iter
        :param key:
        :param value:
        :return:
        """

        def identity(element):
            return element

        if not key:
            key = identity

        if not value:
            value = identity

        def func(iterable, key_, value_):
            group_by_collection = defaultdict(list)
            for element in iterable:
                (key, value) = (key_(element), value_(element))
                group_by_collection[key].append(value)
            for k in group_by_collection:
                yield (k, list(group_by_collection[k]))

        return Iter(func(self, key, value))

    def reduce(self, reducing_function):
        """
        Get a merged value using an associative reduce function,
        so as to reduce the iterable to a single value from left to right.

        :param reducing_function:
        :return:
        """
        return reduce(reducing_function, self)

    def reduce_values(self, reducing_function):
        """
        Make an iterator that returns the merged values for each key using an associative reduce function.
        The values contained in this Iter must be 2-tuples in the form (k, v) where v is Iterable.

        :rtype: Iter
        :param reducing_function:
        :return:
        """

        def reduce_tuple(t):
            return (t[0], Iter(t[1]).reduce(reducing_function))

        return self.map(reduce_tuple)

    def reduce_pair_by_key(self, reducing_function):
        """
        Make an iterator that returns the merged values for each key using an associative reduce function.
        The values contained in this Iter must be 2-tuples in the form (k, v) where v is Iterable.

        :rtype: Iter
        :param reducing_function:
        :return:
        """

        return self \
            .groupby(lambda x: x[0], lambda x: x[1]) \
            .map(lambda (k, v):
                 (k, Iter(v).reduce(reducing_function))
        )

    def union(self, *iterable):
        """
        Make an iterator that returns elements from the first iterable until it
        is exhausted, then proceeds to the next iterable, until all of the iterables
        are exhausted. Used for treating consecutive sequences as a single sequence.

        :rtype Iter:
        :param iterable:
        :return:
        """
        return Iter(it.chain(self._iter, *iterable))

    def slice(self, *args):
        """
        Make an iterator that returns selected elements from the iterable. If start is non-zero, then elements from
        the iterable are skipped until start is reached. Afterward, elements are returned consecutively unless step is
        set higher than one which results in items being skipped. If stop is None, then iteration continues until the
        iterator is exhausted, if at all; otherwise, it stops at the specified position. Unlike regular slicing,
        slice() does not support negative values for start, stop, or step.

        :rtype : Iter
        :param args:
        :return:
        """
        return Iter(it.islice(self._iter, *args))

    def take(self, max):
        """
        Make and iterator that returns the first max elements from the original iterable

        :rtype : Iter
        :param max:
        :return:
        """

        def func(iterable):
            for i, e in enumerate(iterable):
                if i < max:
                    yield e

        return Iter(func(self))

    def sort(self, cmp=None, key=None, reverse=False):
        """
        Make and iterator that is sorted on a specific key, if key is None, sort on
        natural ordering.

        :rtype: Iter
        :param key:
        :return:
        """

        sorted_iterable = sorted(self._iter, cmp=cmp, key=key, reverse=reverse)

        def func(iterable):
            for i in iterable:
                yield i

        return Iter(func(sorted_iterable))

    def top(self, k=1, key=None):
        """
        Make an iterable of the top k elements of the original iterable sorted on keyfunc, if keyfunc is None sort
        on the natural ordering.

        :rtype: Iter
        :type k: int
        :param k:
        :return:
        """

        top_k_values = []

        if k == 1:
            return max(self._iter, key)

        for i, e in enumerate(self._iter):
            if i < k:
                top_k_values.append(e)
            elif i == k:
                heapify(top_k_values)
            elif i > k:
                heapreplace(top_k_values, e)

        return Iter(sorted(top_k_values, key=key, reverse=True))

    def count(self):
        """
        Counts all the elements of the original iterable

        :rtype: int
        :return:
        """
        return len(self._iter)

    def distinct(self):
        """
        Make an iterator with only the distinct elements of the previous.

        :rtype : Iter
        :return:
        """

        def func(iterable):
            # This iterator simply puts elements into a set and looks for
            # simple set membership. Bloom filter implementation may be of interest
            set_of_distinct_values = set()
            for i in iterable:
                if i not in set_of_distinct_values:
                    set_of_distinct_values.add(i)
                    yield i

        return Iter(func(self))

    def distinct_approx(self, init_cap=200, err_rate=0.001):
        """
        Make an iterator with only the distinct elements of the previous.
        Uses a Bloom filter for better space efficiency at the cost of false positive

        :rtype : Iter
        :return:
        """
        try:
            from pybloom import ScalableBloomFilter
        except ImportError:
            print "Unable to import pybloom resorting to traditional distinct"
            return self.distinct()

        def func(iterable):
            # This iterator uses a Bloom filter to check for uniqueness, much more memory efficient
            set_of_distinct_values = ScalableBloomFilter(init_cap, err_rate)
            for element in iterable:
                if element not in set_of_distinct_values:
                    set_of_distinct_values.add(element)
                    yield element

        return Iter(func(self))

    def cache(self):
        """
        Clone the iterable to produce a deepcopy. This may be desired if we wish
        to maintain the state of the iterator while also calling a method with side effects.

        :rtype : Iter
        :return:
        """
        return deepcopy(self)

    def collect(self):
        """
        Collect the iterable back into a list.

        :rtype : list
        :return:
        """
        return list(self)

    @property
    def _(self):
        """
        Collect the iterable back into a list.
        This is really just for some cuteness of syntax

        :rtype : list
        :return:
        """
        return self.collect()

    def __iter__(self):
        for item in self._iter:
            yield item


