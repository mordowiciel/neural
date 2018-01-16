#!/usr/bin/env python

import numpy as np
import pandas as pd
import dataset_utils as du
import argparse

from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
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
dataset_matrix = dataset.as_matrix()

# Standarize the data.
if(NORMALIZE_BOOL_ARG is True):
    dataset_matrix[:, :-1] = preprocessing.scale(dataset_matrix[:, :-1])

# Split the dataset matrix to data and labels array
data = dataset_matrix[:, :-1]
labels = dataset_matrix[:, -1]

# Split data to folds.
skf = StratifiedKFold(n_splits=3)
skf.get_n_splits(data, labels)

confusion_matrixes = []

for train_index, test_index in skf.split(data, labels):

    # Convert data and labels array to tuple format.
    training_data, test_data = du.convert_to_data_tuple(data, labels,
                                                        train_index,
                                                        test_index)
    # Init KNN classifier.
    knn = KNN(training_data, test_data, set(labels),
              NUMBER_OF_NEIGHBOURS_ARG,
              METRIC_ARG)

    # Perform classification task.
    cm = du.create_confusion_matrix(knn, test_data)
    confusion_matrixes.append(cm)

    # Print confusion matrix.
    du.print_cm_info(cm, labels)


# Get the sum confusion matrix from k-fold.
sum_cm = np.sum(confusion_matrixes, axis=0)
du.plot_confusion_matrix(NUMBER_OF_NEIGHBOURS_ARG,
                         METRIC_ARG,
                         DATASET_ARG,
                         NORMALIZE_BOOL_ARG,
                         sum_cm.astype(int),
                         classes=set(labels),
                         title='Confusion matrix')
print ""
