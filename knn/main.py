#!/usr/bin/env python

from sklearn.datasets import load_iris
import distance_utils
import numpy as np

iris_dataset = load_iris()

print iris_dataset.data[0]
print iris_dataset.data[1]

print distance_utils.calculate_euclidean_distance(iris_dataset.data[0],
                                                  iris_dataset.data[1])

print distance_utils.calculate_euclidean_distance(np.array([1, 0]),
                                                  np.array([0, 0]))
