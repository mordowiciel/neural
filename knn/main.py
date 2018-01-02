"""Main file of KNN program."""

# !/usr/bin/env python

from sklearn.datasets import load_iris
import distance_utils

iris_dataset = load_iris()

print iris_dataset.data[0]
print iris_dataset.data[1]

print distance_utils.calculate_euclidean_distance(iris_dataset.data[0],
                                                  iris_dataset.data[1])
