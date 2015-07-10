# -*- coding: utf-8 -*-

"""
itpy.transforms
~~~~~~~~~~~~~~~

This module contains the all the combinators and other methods allowed on
iterables. All functions must consume iterables as it's first argument
and return and an iterable.

"""

from collections import defaultdict
import itertools as it
import types

from lambdas import identity


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
    Make an iterable from the original one but intercept the value and
    evaluate the function for the value.
    This may be valuable for logging and debuging.

    :param iterable:
    :param function:
    """

    def intercepting(iterable_):
        for item in iterable_:
            function(item)
            yield item

    return intercepting(iterable)


def diff(iterable1, iterable2):
    """
    Makes an iterator of the multiset difference between
    two iterables

    :param iterable1:
    :param iterable2:
    :return:
    """
    pass


def drop(iterable, n):
    """
    Make and iterator of the original iterator without the first n elements

    :param iterable:
    :param n:
    :return:
    """
    i = 0
    for element in iterable:
        if i < n:
            i += 1
        else:
            yield element


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


def filter(iterable, predicate):
    """
    Make an iterator that filters elements from iterable returning only those
    for which the predicate is True
    If predicate is None, return the items that are true.

    :param iterable:
    :param predicate:
    """

    for x in iterable:
        if predicate(x):
            yield x


def filterfalse(iterable, predicate):
    """
    Make an iterator that filters elements from iterable returning only those
    for which the predicate is False.
    If predicate is None, return the items that are false

    :param iterable:
    :param predicate:
    """
    for x in iterable:
        if not predicate(x):
            yield x


# TODO
def find(iterable, predicate):
    """
    Produce the first element in the iterable that satisfies the predicate

    :param iterable:
    :param predicate:
    """
    for element in iterable:
        if predicate(element):
            return element


def flatmap(iterable, function_to_list):
    """
    Make an iterator that returns the elements of the lists produced
    by mapping function_to_list onto the original iterable.

    :param iterable:
    :param function_to_list:
    """
    for element in iterable:
        list_block = function_to_list(element)
        for result_value in list_block:
            yield result_value


def flatten(iterable):
    """
    Make an iterator from a iterable of iterables

    :param iterable:
    """
    for element_iterable in iterable:
        for element in element_iterable:
            yield element


def fold(iterable, func):
    """
    Folds the elements of this iterable using an associative binary operator

    :param iterable:
    :param func:
    """
    pass


def forall(iterable, predicate):
    """
    Test if predicate holds for all elements in iterator

    :param iterable:
    :param predicate:
    :return:
    """
    for element in iterable:
        if not predicate(element):
            return False
    return True


def groupby(iterable, key=identity, value=identity):
    """
    Make a dict that returns consecutive keys and groups from the iterable
    The key is computed each element by keyfunc.

    :param iterable:
    :param key:
    """

    group_by_collection = defaultdict(list)
    for element in iterable:
        k = key(element)
        if isinstance(value, types.FunctionType):
            group_by_collection[k].append(value(element))
        else:
            group_by_collection[k].append(value)

    return group_by_collection


def grouped(iterable, n):
    """
    Make an iterator of elements partitioned by the n
    :param iterable:
    :param n:
    """
    batch_window = [None for _ in range(n)]
    cur_size = 0
    for item in iterable:
        batch_window[cur_size] = item
        cur_size += 1
        if cur_size >= n:
            batched = batch_window[:]
            batch_window = [None for _ in range(n)]
            cur_size = 0
            yield batched


def hasDefiniteSize(iterable):
    """
    Tests whether an iterable is know to have a finite size

    :param iterable:
    """
    return hasattr(iterable, '__len__')


def map(iterable, function):
    """
    Make an iterator that computes the function using arguments
    from the original iterable.

    :param iterable:
    :param function:
    """
    for x in iterable:
        yield function(x)


# TODO
def max(iterable):
    """

    :param iterable:
    :return:
    """
    pass


# TODO
def maxBy(iterable, function):
    """

    :param iterable:
    :param function:
    """
    pass


# TODO
def min(iterable):
    """

    :param iterable:
    :return:
    """
    pass


# TODO
def minBy(iterable, function):
    """

    :param iterable:
    :param function:
    """
    pass


def partition(iterable, predicate):
    """
    Partitions this an iterable collection
    in two traversable collections according to a predicate.

    :param iterable:
    :param predicate:
    """
    passes = list()
    fails = list()
    for element in iterable:
        if predicate(element):
            passes.append(element)
        else:
            fails.append(element)
    return passes, fails


# TODO
def permutations(iterable):
    """
    Makes iterable from permutations of iterable

    :param iterable:
    """
    pass


# TODO
def intersect(iterable1, iterable2):
    """
    Returns iterable of the multiset intersection of two iterables

    :param iterable1:
    :param iterable2:
    """
    pass


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


def size(iterable):
    """
    Return the size of the iterable, None if has no attr `__len__`

    :param iterable:
    """
    try:
        return iterable.__len__()
    except AttributeError:
        return None


def sort(iterable, cmp=None, key=None, reverse=False):
    """
    Make and iterator that is sorted on a specific key, if key is None, sort on
    natural ordering.

    :param iterable:
    :param cmp:
    :param key:
    :param reverse:

    TODO: Make lazy

    """
    sorted_iterable = sorted(iterable, cmp=cmp, key=key, reverse=reverse)

    return iter(sorted_iterable)


def top(iterable, max_size=1, key=None):
    """
    Make an iterable of the top max_size elements of the original iterable
    sorted on keyfunc, if keyfunc is None sort on the natural ordering.

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


def take(iterable, n):
    """
    Make an iterator that contains the first n elements from the original

    :param iterable:
    :param n:
    """

    def taking(iterable_):
        for i, e in enumerate(iterable_):
            if i < n:
                yield e

    return taking(iterable)


def takewhile(iterable, predicate):
    """
    Make an iterator that returns elements from the iterable as long as the
    predicate is true.

    :param iterable:
    :param predicate:
    """
    return iter(it.takewhile(predicate, iterable))


def toArray(iterable):
    import array
    return array.array(iterable)


def toList(iterable):
    return list(iterable)


def union(iterable, *iterables):
    """
    Make an iterator that returns elements from the first iterable until it
    is exhausted, then proceeds to the next iterable, until all of the iterables
    are exhausted. Used for treating consecutive sequences as a single sequence.

    :param iterable:
    :param iterables:
    """
    return iter(it.chain(iterable, *iterables))
