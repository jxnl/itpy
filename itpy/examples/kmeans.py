# -*- coding: utf-8 -*-
"""
itpy.examples.kmeans
~~~~~~~~~~~~~~~~~~~~~~~

This is an example of a naive kmeans implementation for for 2d vectors
"""

from __future__ import print_function

from os.path import join, dirname
from random import random

from itpy import Itpy
from itpy.lambdas import str_split, str_strip


fn = str(join(dirname(__file__), 'data_for_kmeans.csv'))


def dist(point1, point2):
    """
    Calculate the euclidian distance between two points

    :param point1:
    :param point2:
    """
    return sum((x - y) ** 2 for x, y in zip(point1, point2))


def which_centroid(centroids):
    """
    Consume centroids and return a function that classifys the a point

    :param centroids:
    """
    def classifer(point):
        for clazz, centroid in enumerate(centroids):
            cur_dist = dist(centroid, point)
            if clazz == 0:
                best_distance = cur_dist
                best_clazz = 0
            else:
                if best_distance > cur_dist:
                    best_distance = cur_dist
                    best_clazz = clazz
        return best_clazz

    return classifer


def centroid_of(points):
    """
    Consumes a list of points and finds the new centroid

    :param points:
    :return:
    """
    n = len(points)
    summed_points = Itpy(points) \
        .reduce(lambda p1, p2: (p1[0] + p2[0], p1[1] + p2[1]))
    centroid = (summed_points[0] / n, summed_points[1] / n)
    return centroid

# Initalize centroids
current_centroids = [
    (random(), random()),
    (random(), random())
]

# Iterate and redefine the centroids
for _ in range(10):
    current_centroids = Itpy.from_file(fn)\
        .map(str_strip)\
        .map(str_split(","))\
        .map(lambda (x, y): (float(x), float(y)))\
        .groupby(key=which_centroid(current_centroids))\
        .map(lambda (clazz, points): centroid_of(points))\
        ._

print(current_centroids)

