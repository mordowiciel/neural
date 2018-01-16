import math


def euclidean_distance(arr1, arr2):

    if(arr1.size != arr2.size):
        raise ValueError("Arrays vary in size")

    distance_sum = 0
    for n in range(0, arr1.size):
        distance_sum += pow((arr1[n] - arr2[n]), 2)

    return math.sqrt(distance_sum)


def manhattan_distance(arr1, arr2):

    if(arr1.size != arr2.size):
        raise ValueError("Arrays vary in size")

    distance_sum = 0
    for n in range(0, arr1.size):
        distance_sum += abs(arr1[n] - arr2[n])

    return distance_sum


def chebyshev_distance(arr1, arr2):

    if(arr1.size != arr2.size):
        raise ValueError("Arrays vary in size")

    result_arr = []
    for n in range(0, arr1.size):
        result_arr.append(abs(arr1[n] - arr2[n]))

    return max(result_arr)
