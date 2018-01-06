import distance_utils as du
import heapq


class KNN:

    knn_heap = []
    training_data = []
    test_data = []
    k = 0

    def __init__(self, training_data, test_data, k):
        self.training_data = training_data
        self.test_data = test_data
        self.k = k

    def init_point_heap(self, test_point):

        for point in self.training_data:
            distance = du.euclidean_distance(point[0], test_point)
            label_number = point[1]
            heapq.heappush(self.knn_heap, (distance, label_number))

    def classify_point(self, test_point):

        self.knn_heap = []
        self.init_point_heap(test_point)

        class_count = [0, 0, 0]
        for i in range(0, self.k):
            neighbour = heapq.heappop(self.knn_heap)

            if(neighbour[1] == 0):
                class_count[0] += 1
            if(neighbour[1] == 1):
                class_count[1] += 1
            if(neighbour[1] == 2):
                class_count[2] += 1

        point_class = class_count.index(max(class_count))
        return point_class
