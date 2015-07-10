# -*- coding: utf-8 -*-

"""
itpy.lambdas
~~~~~~~~~~~~

This module contains some helper classes and gives  names to lambda expressions for readability

"""


def not_none(x):
    return (x is not None)


def identity(x):
    return x


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mull(x, y):
    return x * y


def rdiv(x, y):
    return x / y


def ldiv(x, y):
    return x / y


def one(x):
    return 1


def keyf(x):
    assert len(x) == 2
    return x[0]


def valuef(x):
    assert len(x) == 2
    return x[1]


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
