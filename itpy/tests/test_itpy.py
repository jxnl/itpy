# -*- coding: utf-8 -*-

"""
test_itpy
~~~~~~~~~

These are some tests... Nothing to see here unless you also want to take a look at what each thing will do.
For these tests you will notice that ._ is being called. this results in the termination of a series of transformations

"""

import unittest

from itpy import Itpy as _

class test_itpy(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)
        self.mapf = lambda x: x ** 2
        self.filterf = lambda x: x % 2 == 0
        self.flatmapf = lambda x: [x, x + 1, x + 2]
        self.takewhilef = lambda x: x < 5
        self.dropwhilef = lambda x: x < 5
        self.evenf = lambda x: x % 2
        self.sumf = lambda x, y: x + y

    def test_map(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.map(self.mapf)._,
            map(self.mapf, self.seq)
        )

    def test_filter(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.filter(self.mapf)._,
            filter(self.mapf, self.seq)
        )

    def test_fmap(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.flatmap(self.flatmapf)._,
            reduce(self.sumf, map(self.flatmapf, self.seq))
        )

    def test_takewhile(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.takewhile(self.takewhilef)._,
            self.seq[:5]
        )

    def test_dropwhile(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.dropwhile(self.dropwhilef)._,
            self.seq[5:]
        )

    def test_groupby(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.groupby(self.evenf)._,
            [(0, [0, 2, 4, 6, 8]),
             (1, [1, 3, 5, 7, 9])]
        )

    def test_flat_reduce(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.reduce(self.sumf),
            sum(self.seq)
        )

    def test_union(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.union(self.seq).union(self.seq)._,
            self.seq * 3
        )

    def test_slice_start(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.slice(5)._,
            self.seq[:5]
        )

    def test_slice_start_end(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.slice(5, 8)._,
            self.seq[5:8]
        )

    def test_slice_start_end_skip(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.slice(2, 8, 3)._,
            self.seq[2:8:3]
        )

    def test_take(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.take(3)._,
            self.seq[:3]
        )

    def test_over_take(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.take(3000)._,
            self.seq
        )

    def test_sort(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.sort(reverse=True)._,
            sorted(self.seq, reverse=True)
        )

    def test_top(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.top(2)._,
            sorted(self.seq, reverse=True)[:2]
        )


    def test_over_top(self):
        lst = _(self.seq)
        self.assertEqual(
            lst.top(10000)._,
            sorted(self.seq, reverse=True)
        )


if __name__ == '__main__':
    unittest.main()
