"""Main file of KNN program."""

# !/usr/bin/env python

from sklearn.datasets import load_iris
import numpy as np
from knn import KNN

# Load dataset and init training and test data.
iris_dataset = load_iris()
data = zip(iris_dataset.data, iris_dataset.target)
np.random.shuffle(data)
training_data = data[:100]
test_data = data[100:]

properly_classified = 0
knn = KNN(training_data, test_data, 3)

for point in test_data:

    classification_label = knn.classify_point(point[0])
    if(point[1] == classification_label):
        properly_classified += 1

print "Properly classifed : ", properly_classified, "/", len(test_data)
