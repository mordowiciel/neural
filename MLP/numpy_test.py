import numpy as np

matrix1 = np.array([2, 2])
matrix2 = np.array([[1, 2], [3, 4], [5, 6]])

vector = np.array([[1, 2]])

# print('Row vector')
# print(vector)
#
# print('Column vector')
# print(vector.transpose())

# print('Before transpose')
# print(matrix2)
#
# print('After: ')
# print(matrix2.transpose())

def calculate_output_with_sigmoidal(input):
    weights = np.array([[0.5, 0.4]])
    neuronSum = np.sum(weights * input)
    return neuronSum

dataInput = np.array([[1.5, 1.7]])
print calculate_output_with_sigmoidal(dataInput)