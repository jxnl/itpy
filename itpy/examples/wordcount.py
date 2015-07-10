# -*- coding: utf-8 -*-
"""
itpy.examples.wordcount
~~~~~~~~~~~~~~~~~~~~~~~

This is an example of a wordcount program that reads in a text file.

1) flatmap a split
2) map a strip
3) reduceby actually does both map and reduce...
    map to (k, 1)
    reduce 1s to count
4) sort on value
5) push to stdout

"""

from __future__ import print_function

from os.path import join, dirname

from itpy import Itpy
from itpy.helpers import str_split, str_strip, identity, one, add, valuef, pair_to_str


file_name = str(join(dirname(__file__), 'zen.txt'))

tokenized = Itpy.from_file(file_name) \
    .flatmap(str_split(" ")) \
    .map(str_strip) \
    .reduceby(reducer=add, key=identity, value=one) \
    .sort(key=valuef, reverse=True)

tokenized.map(pair_to_str).to_stdout()
