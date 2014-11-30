# -*- coding: utf-8 -*-

from __future__ import print_function

from os.path import join, dirname

from itpy import Itpy
from itpy.lambdas import str_split, str_strip, identity, one, add, valuef, pair_to_str


fn = str(join(dirname(__file__), 'zen.txt'))

tokenized = Itpy.from_file(fn)\
    .flatmap(str_split(" "))\
    .map(str_strip)\
    .reduceby(reducer=add, key=identity, value=one)\
    .sort(key=valuef, reverse=True)\

tokenized.map(pair_to_str).to_stdout()
