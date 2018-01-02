"""Main file of KNN program."""

# !/usr/bin/env python

from sklearn.datasets import load_iris
import distance_utils as du

iris_dataset = load_iris()

print iris_dataset.data[0]
print iris_dataset.data[1]

print 'Euclidean distance: '
print du.euclidean_distance(iris_dataset.data[0],
                            iris_dataset.data[1])

print 'Manhattan distance: '
print du.manhattan_distance(iris_dataset.data[0],
                            iris_dataset.data[1])

print 'Chebyshev distance: '
print du.chebyshev_distance(iris_dataset.data[0],
                            iris_dataset.data[1])
