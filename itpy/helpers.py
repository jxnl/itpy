# -*- coding: utf-8 -*-

"""
itpy.lambdas
~~~~~~~~~~~~

This module contains some helper classes and gives  names to lambda expressions for readability
"""

import types


def not_none(x):
    return (x is not None)


def identity(x):
    return x


def one(x):
    return 1


def number(x):
    def num(y):
        return x

    return num


def get_key(*keys):
    """
    Create a function that takes an object with attributes and
    returns the key:value dictionary

    :param keys:
    :return: function
    """
    def key_getter(obj):
        k = {key:obj[key] for key in keys}
        return k

    return key_getter


def try_or(try_function, orfail, exception=Exception):
    """
    Create a function that will try to call `try_function()` and
    if it fails with `exception`  will call `orfail()` if its a function
    otherwise returns `orfail`

    :param try_function: function
    :param orfail: function
    :param exception: exception
    :return: function
    """
    def try_expression(*args, **kwargs):
        try:
            return try_function(*args, **kwargs)
        except exception:
            if isinstance(orfail, types.FunctionType):
                return orfail(*args, **kwargs)
            return orfail

    return try_expression


def if_else(if_predicate, if_return, else_return):
    """


    :param if_predicate:
    :param if_return:
    :param else_return:
    :return:
    """
    def if_else_expression(*args, **kwargs):
        if if_predicate(*args, **kwargs):
            if isinstance(if_return, types.FunctionType):
                return if_return(*args, **kwargs)
            return if_return
        else:
            if isinstance(else_return, types.FunctionType):
                return else_return(*args, **kwargs)
            return else_return

    return if_else_expression


def str_split(sep=None):
    if not sep:
        sep = " "

    def spliter(string):
        return str(string).split(sep)

    return spliter


def str_strip(s):
    return s.strip()


def pair_to_str(p):
    return "{},{}".format(p[0], p[1])


def getitem(x):
    def getter(obj):
        return obj[x]
    return getter
