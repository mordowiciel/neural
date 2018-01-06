"""Main file of KNN program."""

# !/usr/bin/env python

from sklearn.datasets import load_iris
import numpy as np
import distance_utils as du
import heapq
from itertools import count

# a global
tiebreaker = count()

# Load dataset and init training and test data.
iris_dataset = load_iris()
data = zip(iris_dataset.data, iris_dataset.target)
np.random.shuffle(data)
training_data = data[:100]
test_data = data[100:]


test_point = test_data[0]
print "Test point: " + str(test_point)

# Create heap of training data.
k = 3
knn_heap = []
for point in training_data:
    distance = du.euclidean_distance(point[0], test_point[0])
    label_number = point[1]
    heapq.heappush(knn_heap, (distance, label_number))

# Classify the given test point.
class_count = [0, 0, 0]
for i in range(0, k):
    neighbour = heapq.heappop(knn_heap)
    print str(i) + " neighbour label : " + str(neighbour[1])

    if(neighbour[1] == 0):
        class_count[0] += 1
    if(neighbour[1] == 1):
        class_count[1] += 1
    if(neighbour[1] == 2):
        class_count[2] += 1

    point_class = class_count.index(max(class_count))

print "Classified label ", point_class
