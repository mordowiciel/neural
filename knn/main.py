"""Main file of KNN program."""

# !/usr/bin/env python

import numpy as np
import pandas as pd
import dataset_utils as du
from sklearn import preprocessing
from knn import KNN

# Load dataset.
dataset = pd.read_csv("iris.csv", header=None)
data = dataset.as_matrix()
np.random.shuffle(data)

# Standarize the data.
data[:, :-1] = preprocessing.scale(data[:, :-1])

# Get classification labels from dataset,
# convert matrix to (data, label) tuple.
class_labels = du.get_classification_labels(data)
data = du.convert_to_point_label_tuple(data)

# Perform k-cross validation
for i in range(0, 3):

    print 10 * "*", "K = ", i, 10 * "*"
    properly_classified = 0

    # Create training_data and test_data sets
    training_data, test_data = du.divide_k_cross(data, i)
    knn = KNN(training_data, test_data, class_labels, 3)

    for point in test_data:

        classification_label = knn.classify_point(point[0])
        print "Expected class:", point[1], "Result:", classification_label

        if(point[1] == classification_label):
            properly_classified += 1

    print "Properly classifed : ", properly_classified, "/", len(test_data)
