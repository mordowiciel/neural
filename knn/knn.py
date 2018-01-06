import distance_utils as du
import heapq


def init_point_heap(training_data, test_point):

    knn_heap = []
    for point in training_data:
        distance = du.euclidean_distance(point[0], test_point[0])
        label_number = point[1]
        heapq.heappush(knn_heap, (distance, label_number))

    return knn_heap


def classify_point(knn_heap, test_point, k):

    class_count = [0, 0, 0]
    for i in range(0, k):
        neighbour = heapq.heappop(knn_heap)

        if(neighbour[1] == 0):
            class_count[0] += 1
        if(neighbour[1] == 1):
            class_count[1] += 1
        if(neighbour[1] == 2):
            class_count[2] += 1

    point_class = class_count.index(max(class_count))
    return point_class
