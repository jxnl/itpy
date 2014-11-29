# -*- coding: utf-8 -*-

"""
itpy.sketch
~~~~~~~~~~~

This module contains functions that compute sketchs over the iterable.
This means that to allow for sublinear space effeciency we trade a bit of accuracy for performance

"""

from pybloom import ScalableBloomFilter


def count_distinct_approx(iterable, init_cap=200, err_rate=0.001):
    """
    Count the number of distinct elements from an iterable. This implementation uses a bloomfilter to approximate
    the number of distinct values found in this iterable.
    
    :param iterable:
    :param init_cap:
    :param err_rate:
    """

    counter = 0

    set_of_distinct_values = ScalableBloomFilter(init_cap, err_rate)

    for element in iterable:
        if element not in set_of_distinct_values:
            set_of_distinct_values.add(element)
            counter += 1

    return counter


def frequency_approx(iterable, table_width=1000, n_hashs=10):
    """
    Count the frequency of each type of event. This implementation uses a count-min to approximate the
    occurences of each distinct alue found in this iterable.

    :param iterable:
    :param table_width:
    :param n_hashs:
    """
    raise NotImplementedError


def to_bloomfilter(iterable, init_cap=200, err_rate=0.001):
    """
    Converts the iterable into a ScalableBloomFilter
    
    :rtype : pybloom.ScalableBloomFilter
    :param iterable:
    :param init_cap:
    :param err_rate:
    """

    bloom = ScalableBloomFilter(init_cap, err_rate)
    for element in iterable:
        bloom.add(element)

    return bloom