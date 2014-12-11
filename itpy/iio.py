# -*- coding: utf-8 -*-
"""
itpy.iio
~~~~~~~~

This module contains methods for different I/O requirements.
"""

from __future__ import print_function

def from_file(path_to_file, buffer=1):
    """
    Make an iterable from the file that the path points to, the arguments mirrors how open() is implemented
    The optional buffering argument specifies the file’s desired buffer size: 0 means unbuffered,  1 means line
    buffered, any other positive value means use a buffer of (approximately) that size (in bytes).

    :param path_to_file:
    :param buffer:
    """
    with open(path_to_file, buffering=buffer) as buffered_file:
        for line in buffered_file:
            yield line


def from_stdin():
    """
    Make an iterable from standard inpurt
    """
    from sys import stdin

    for line in stdin:
        yield line


def to_file(iterable, path_to_file, mode="w+"):
    """
    Write iterable to file.

    :param iterable:
    :param path_to_file:
    :param mode:
    """
    with open(path_to_file, mode) as target:
        for line in iterable:
            target.write(str(line) + "\n")


def to_stdout(iterable):
    from sys import stdout

    for line in iterable:
        stdout.write(str(line) + "\n")


def to_print(iterable):
    for line in iterable:
        print(line)
