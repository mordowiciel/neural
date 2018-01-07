"""Main file of KNN program."""

# !/usr/bin/env python

# from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
from knn import KNN

# Load dataset and init training and test data.
dataset = pd.read_csv("wine.csv", header=None)
data = dataset.as_matrix()
np.random.shuffle(data)

# Create (point, label) tuple
data_tuples = []
class_labels = set([])
for row in data:

    # Extract labels from dataset
    class_labels.add(row[-1])

    row_tuple = (row[:-1], row[-1])
    data_tuples.append(row_tuple)

data = data_tuples

training_data = data[:100]
test_data = data[100:]

properly_classified = 0
knn = KNN(training_data, test_data, class_labels, 3)

for point in test_data:

    classification_label = knn.classify_point(point[0])
    print "Expected class:", point[1], "Result:", classification_label

    if(point[1] == classification_label):
        properly_classified += 1

print "Properly classifed : ", properly_classified, "/", len(test_data)
