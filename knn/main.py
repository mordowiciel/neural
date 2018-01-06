"""Main file of KNN program."""

# !/usr/bin/env python

from sklearn.datasets import load_iris
import numpy as np
import knn

# Load dataset and init training and test data.
iris_dataset = load_iris()
data = zip(iris_dataset.data, iris_dataset.target)
np.random.shuffle(data)
training_data = data[:100]
test_data = data[100:]

properly_classified = 0
for test_point in test_data:

    knn_heap = knn.init_point_heap(training_data, test_point)
    point_class = knn.classify_point(knn_heap, test_point, k=3)

    if(point_class == test_point[1]):
        properly_classified += 1

print "Properly classified :", properly_classified, "/", len(test_data)
