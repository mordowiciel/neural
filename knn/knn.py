import heapq
import distance_utils as du


class KNN:

    knn_heap = []
    training_data = []
    test_data = []
    classification_labels = set()
    k = 0
    metric = ''

    def __init__(self, training_data, test_data, class_labels, k, metric):
        self.training_data = training_data
        self.test_data = test_data
        self.classification_labels = class_labels
        self.k = k
        self.metric = metric

    def init_point_heap(self, test_point):

        for point in self.training_data:

            distance = 0
            print self.metric

            if(self.metric == "euclidean"):
                distance = du.euclidean_distance(point[0], test_point)
            if(self.metric == "manhattan"):
                distance = du.manhattan_distance(point[0], test_point)
            if(self.metric == "chebyshev"):
                distance = du.chebyshev_distance(point[0], test_point)

            label_number = point[1]
            heapq.heappush(self.knn_heap, (distance, label_number))

    def classify_point(self, test_point):

        self.knn_heap = []
        self.init_point_heap(test_point)

        # init dictionary
        class_count = {}
        for label in self.classification_labels:
            class_count[label] = 0

        for i in range(0, self.k):
            neighbour = heapq.heappop(self.knn_heap)
            class_count[neighbour[1]] += 1

        return max(class_count, key=class_count.get)
