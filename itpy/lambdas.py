# -*- coding: utf-8 -*-

"""
itpy.lambdas
~~~~~~~~~~~~

This module contains some helper classes and gives  names to lambda expressions for readability

"""

def not_none(x):
    return (x != None)

def identity(x):
    return x

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def sub(x, y):
    return y-x

def mull(x, y):
    return x*y

def rdiv(x, y):
    return x/y

def ldiv(x, y):
    return x/y

def one(x):
    return 1

def keyf(x):
    assert len(x) == 2
    return x[0]

def valuef(x):
    assert len(x) == 2
    return x[1]
