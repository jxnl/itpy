# -*- coding: utf-8 -*-

"""
itpy.summary
~~~~~~~~~~~

"""
from __future__ import division


def reduce_(iterable, reducer):
    """
    Get a merged value using an associative reduce function,
    so as to reduce the iterable to a single value from left to right.
    """
    value = iterable.next()

    for rest in iterable:
        value = reducer(value, rest)

    return value

def count(iterable):
    """
    Counts all the elements of the original iterable
    """
    length = len(iterable)
    return length

def mean(iterable):
    """
    Computes the mean with a single pass of the iterable.
    """
    size_accumilator = 0
    sum_of_values = 0

    for x in iterable:
        sum_of_values += x
        size_accumilator += 1

    # Practice safe division.
    if (size_accumilator < 2):
        return 0

    ret_result = sum_of_values / size_accumilator
    return ret_result

def twopass_variance(iterable):
    """
    Computes the variance with two passes of the iterable,
    once to calculate the mean, next to calculate the sum of squares.
    """
    size_accumilator = 0
    sum_of_squares = 0

    mean_result = mean(iterable)

    for x in iterable:
        size_accumilator += 1
        difference = (x-mean_result)
        sum_of_squares += difference * difference

    # Practice safe division.
    if (size_accumilator < 2):
        return 0

    ret_result = sum_of_squares / (size_accumilator - 1)
    return ret_result

def online_variance(iterable):
    """
    Computes the variance with one pass of the iterable.
    This method allows for partial answers up to the procced value.

    Note, unless your are are certain that your data is shuffled,
    you will not get meaningful partial results.
    """
    size_accumilator = 0
    current_mean = 0
    M2 = 0

    try :
        for x in iterable:
            size_accumilator += 1
            difference = x - current_mean
            current_mean += difference/size_accumilator
            M2 += difference*(x - current_mean)
    except KeyboardInterrupt:
        pass

    # Practice safe division.
    if (size_accumilator < 2):
        return 0

    variance = M2/(size_accumilator - 1)
    return variance