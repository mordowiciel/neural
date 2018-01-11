#!/usr/bin/env python

import numpy as np
import pandas as pd
import dataset_utils as du
import argparse

from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from knn import KNN

# Setup argparse.
parser = argparse.ArgumentParser(description='SISE Zadanie 2 - KNN')
parser.add_argument('--neighbours',
                    type=int,
                    required=True,
                    help="Number of neighbours used in KNN search")
parser.add_argument('--metrics',
                    required=True,
                    help="Metric used to calculate distance between points")
parser.add_argument('--dataset',
                    required=True,
                    help="Dataset to perform KNN")
parser.add_argument('--normalize',
                    action='store_true',
                    required=False,
                    help="Perform data normalization")

args = parser.parse_args()

NUMBER_OF_NEIGHBOURS_ARG = args.neighbours
METRIC_ARG = args.metrics
DATASET_ARG = args.dataset
NORMALIZE_BOOL_ARG = args.normalize

print "Number of neighbours", NUMBER_OF_NEIGHBOURS_ARG
print "Metric", METRIC_ARG
print "Dataset", DATASET_ARG
print "Normalizing", NORMALIZE_BOOL_ARG

# Load dataset.
dataset = pd.read_csv(DATASET_ARG, header=None)
data = dataset.as_matrix()
np.random.shuffle(data)

# Standarize the data.
if(NORMALIZE_BOOL_ARG is True):
    data[:, :-1] = preprocessing.scale(data[:, :-1])

# Get classification labels from dataset,
# convert matrix to (data, label) tuple.
class_labels = du.get_classification_labels(data)
data = du.convert_to_point_label_tuple(data)

# Perform k-cross validation
confusion_matrixes = []
for i in range(0, 3):

    properly_classified = 0
    true_arr = []
    predicted_arr = []

    training_data, test_data = du.divide_k_cross(data, i)
    knn = KNN(training_data,
              test_data,
              class_labels,
              NUMBER_OF_NEIGHBOURS_ARG,
              METRIC_ARG)

    for point in test_data:

        classification_label = knn.classify_point(point[0])

        true_arr.append(point[1])
        predicted_arr.append(classification_label)

        if(point[1] == classification_label):
            properly_classified += 1

    print "Properly classifed : ", properly_classified, "/", len(test_data)
    cm = confusion_matrix(true_arr, predicted_arr)
    print cm
    confusion_matrixes.append(cm)

# Get the sum confusion matrix from k-fold.
average_cm = np.sum(confusion_matrixes, axis=0)
# du.plot_confusion_matrix(average_cm.astype(int), classes=class_labels,
#                          title='Confusion matrix')
print ""
