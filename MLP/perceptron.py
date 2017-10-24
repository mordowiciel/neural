import numpy as np


class Perceptron:

    def __init__(self):
        self.weights = np.array([])
        self.output = 0

    def calculate_output_with_linear(self, input):

        if len(self.weights) == 0:
            self.weights = np.random.rand(len(input))

        return np.sum(self.weights * input)

    def calculate_output_with_sigmoidal(self, input):

        if len(self.weights) == 0:
            self.weights = np.random.rand(len(input))

        neuron_sum = np.sum(self.weights * input)
        return neuron_sum * (1 - neuron_sum)
