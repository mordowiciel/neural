import numpy as np


class Perceptron:

    def __init__(self):
        self.weights = np.array([])
        self.output = 0
        self.error_value = 0
        self.hasBias = True

    def calculate_output_with_linear(self, input):

        if len(self.weights) == 0:

            if self.hasBias:
                self.weights = np.random.rand(len(input) + 1)
                input = np.append(input, [1])
                print(input)
            else:
                self.weights = np.random.rand(len(input))

        return np.sum(self.weights * input)

    def calculate_output_with_sigmoidal(self, input):

        if len(self.weights) == 0:

            if self.hasBias:
                self.weights = np.random.rand(len(input) + 1)
                input = np.append(input, [1])
                print(input)
            else:
                self.weights = np.random.rand(len(input))

        neuron_sum = np.sum(self.weights * input)
        return neuron_sum * (1 - neuron_sum)

    def __str__(self):
        return 'Output : ' + str(self.output)

    def __repr__(self):
        return 'classPerceptron object output : ' + str(self.output)