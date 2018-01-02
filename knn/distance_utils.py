import math


def calculate_euclidean_distance(arr1, arr2):

    if(arr1.size != arr2.size):
        raise ValueError("Arrays vary in size")

    distance_sum = 0
    for n in range(0, arr1.size):
        distance_sum += pow((arr1[n] - arr2[n]), 2)

    return math.sqrt(distance_sum)
