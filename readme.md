itpy.py
=========

![https://travis-ci.org/jxnl/itpy.svg?branch=master](https://travis-ci.org/jxnl/itpy.svg?branch=master)

Built on the back of itertools, `itpy` allows easy list processing through chaining methods.
Everything is a lazy evaluated generating function so nothing happens until you call a method
with side effects. This allows for a fast memory effecient 'keep what you need' way of processing
large ammounts of data!


## Installation

Its not ready for PyPi yet so you'd have to just clone and run the following command.

    python setup.py install

## Getting Started

For syntactic preference, you can either collect the generator into a list by calling `itpy._`

```python
# this is only for personal preference
from itpy import Itpy
```
##### Apply a map!
```python
lst = Itpy([1,2,3]).map(lambda x: x**2)._
# [1,4,9]
```
##### Apply a groupby on tuples!
```python
# note that without a keyf, valuef, we implicitly assume they are tuples.
lst = Itpy([(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (1, 5)]).groupby()._
# [(0, [(0, 0), (0, 2), (0, 4)]),
#  (1, [(1, 1), (1, 3), (1, 5)])]
```

##### Apply an arbitrary key function under a groupby!

Note that for some methods they accept a `key` and `value` and are otherwise null.
If they are `None` both will return the original object. If they are not, each element will look like a pair `Tuple(key(x), value(x))`

```python
lst = Itpy(xrange(0,6)).groupby(lambda x: x%2)._
# [(0, [0, 2, 4]),
#  (1, [1, 3, 5])]
```
##### Takes advantage of some streaming algorithms!

I'd love to see you contribute more streaming algorithms too!

```python
# uses a heapqueue!
lst = Itpy(huge_list_of_values).top(10)._
# uses set.contains()!
lst = Itpy(huge_list_of_values).distinct()._
# uses reservoir sampling!
lst = Itpy(huge_list_of_values).sample_without_replacement(10)._
```

## Digging deeper

This is partly inspired by how much fun it was to write spark jobs.
If you want to request a feature or submit a feature, write up a method, write up some tests and make a pull request!

I'd really like to see some interesting streaming algorithms!
