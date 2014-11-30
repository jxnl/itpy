# -*- coding: utf-8 -*-

"""
itpy.transforms
~~~~~~~~~~~~~~~

This module contains the all the closed transformations on iterables.
All functions must consume iterables as it's first argument and return
and an iterable.

"""

from collections import defaultdict
from lambdas import identity, keyf, valuef

import itertools as it


# noinspection PyShadowingBuiltins
def map(iterable, function):
    """
    Make an iterator that computes the function using arguments
    from the original iterable.

    :param iterable:
    :param function:
    """
    for x in iterable:
        yield function(x)


def flatmap(iterable, function_to_list):
    """
    Make an interator that returns the elements of the lists produced
    by mapping function_to_list onto the original iterable.

    :param iterable:
    :param function_to_list:
    """

    itera = iter(iterable)

    while True:
        list_block = function_to_list(itera.next())
        for result_value in list_block:
            yield result_value


# noinspection PyShadowingBuiltins
def filter(iterable, predicate):
    """
    Make an iterator that filters elements from iterable returning only those
    for which the predicate is True
    If predicate is None, return the items that are true.

    :param iterable:
    :param predicate:
    """
    return iter(it.ifilter(predicate, iterable))


def filterfalse(iterable, predicate):
    """
    Make an iterator that filters elements from iterable returning only those
    for which the predicate is False.
    If predicate is None, return the items that are false

    :param iterable:
    :param predicate:
    """
    return iter(it.ifilterfalse(predicate, iterable))


def takewhile(iterable, predicate):
    """
    Make an iterator that returns elements from the iterable as long as the
    predicate is true.

    :param iterable:
    :param predicate:
    """
    return iter(it.takewhile(predicate, iterable))


def dropwhile(iterable, predicate):
    """
    Make an iterator that drops elements from the iterable as long as the
    predicate is true

    Note, the iterator does not produce any output until the predicate
    first becomes false, so it may have a lengthy start-up time.

    :param iterable:
    :param predicate:
    """
    return iter(it.dropwhile(predicate, iterable))


def groupby(iterable, key=identity, value=identity):
    """
    Make an iterator that returns consecutive keys and groups from the iterable
    The key and value is computed each element by keyfunc and valfunc.
    If these functions are not not specified or is None, default to identity function.

    :param iterable:
    :param key:
    :param value:
    """

    def grouping(iterable_, key_, value_):
        group_by_collection = defaultdict(list)
        for element in iterable_:
            (k, v) = (key_(element), value_(element))
            group_by_collection[k].append(v)
        for k in group_by_collection:
            yield (k, list(group_by_collection[k]))

    return grouping(iterable, key, value)


def reduceby(iterable, reducer, key=keyf, value=valuef):
    """
    Make an iterator that returns the merged values for each key using an
    associative reduce function.The values contained in this iterable must be
    2-tuples in the form (k, v).

    :param iterable:
    :param reducer:
    :param key:
    :param value:
    """
    def reducing(iterable_, reducer_, key_, value_):
        group_by = dict()

        for element in iterable_:
            (k, v) = (key_(element), value_(element))

            if k in group_by:
                group_by[k] = reducer_(group_by[k], v)
            else:
                group_by[k] = v

        for ke in group_by:
            yield (ke, group_by[ke])

    return reducing(iterable, reducer, key, value)


def union(iterable, *iterables):
    """
    Make an iterator that returns elements from the first iterable until it
    is exhausted, then proceeds to the next iterable, until all of the iterables
    are exhausted. Used for treating consecutive sequences as a single sequence.

    :param iterable:
    :param iterables:
    """
    return iter(it.chain(iterable, *iterables))


# noinspection PyShadowingBuiltins
def slice(iterable, *args):
    """
    Make an iterator that returns selected elements from the iterable.
    If start is non-zero, then elements from the iterable are skipped
    until start is reached. Afterward, elements are returned consecutively
    unless step is set higher than one which results in items being skipped.

    If stop is None, then iteration continues until the iterator is exhausted;
    otherwise, it stops at the specified position. Unlike regular slicing,
    slice() does not support negative values for start, stop, or step.

    :param iterable:
    :param args:
    """
    return iter(it.islice(iterable, *args))


def take(iterable, max):
    """
    Make and iterator that returns the first max elements from the original iterable

    :param iterable:
    :param max:
    """
    def taking(iterable_):
        for i, e in enumerate(iterable_):
            if i < max:
                yield e

    return taking(iterable)


def sort(iterable, cmp=None, key=None, reverse=False):
    """
    Make and iterator that is sorted on a specific key, if key is None, sort on
    natural ordering.

    :param iterable:
    :param cmp:
    :param key:
    :param reverse:
    """
    sorted_iterable = sorted(iterable, cmp=cmp, key=key, reverse=reverse)

    return iter(sorted_iterable)


def top(iterable, max_size=1, key=None):
    """
    Make an iterable of the top max_size elements of the original iterable sorted on keyfunc, if keyfunc is None sort
    on the natural ordering.

    :param iterable:
    :param max_size:
    :param key:
    """

    # An import is done here to avoid polluting the namespace
    from heapq import heapreplace, heapify

    top_k_values = []

    for idx, item in enumerate(iterable):
        if idx < max_size:
            top_k_values.append(item)
        elif idx == max_size:
            heapify(top_k_values)
        elif idx > max_size:
            heapreplace(top_k_values, item)

    return iter(sorted(top_k_values, key=key, reverse=True))


def sample(iterable, max_size):
    """
    Make an iterator of `max_size` of randomly sampled elements from the original

    :param iterable:
    :param max_size:
    """
    from random import randint

    reservoir = list()

    for (i, item) in enumerate(iterable):
        switch = randint(0, 1)
        if len(reservoir) < max_size:
            reservoir.append(item)
        elif switch < max_size:
           reservoir[switch] = item

    return iter(reservoir)


def distinct(iterable):
    """
    Make an iterator with only the distinct elements of the previous.

    :param iterable:
    """

    def distincting(iterable_):
        set_of_distinct_values = set()
        for i in iterable_:
            if i not in set_of_distinct_values:
                set_of_distinct_values.add(i)
                yield i

    return distincting(iterable)

def intercept(iterable, function):
    """
    Make an iterable from the original one but intercept the value and evaluate the function for the value.
    This may be valuable for logging and debuging.

    :param iterable:
    :param function:
    """
    def intercepting(iterable_):
        for i in iterable_:
            function(i)
            yield i
    return intercepting(iterable)
