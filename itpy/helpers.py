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
    def key_getter(obj):
        k = obj
        for key in keys:
            k = k[key]
        return k

    return key_getter


def try_or(try_f, orfail, exception=Exception):
    def try_expression(obj):
        try:
            return try_f(obj)
        except exception:
            if isinstance(orfail, types.FunctionType):
                return orfail(obj)
            return orfail

    return try_expression


def if_else(if_predicate, if_return, else_return):
    def if_else_expression(obj):
        if if_predicate(obj):
            if isinstance(if_return, types.FunctionType):
                return if_return(obj)
            return if_return
        else:
            if isinstance(else_return, types.FunctionType):
                return else_return(obj)
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
