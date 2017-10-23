import numpy as np


class Perceptron:
    def __init__(self):
        self.weights = []
        self.output = 0

    def calculate_output_with_linear(self, input):

        if len(self.weights) == 0:
            print 'CALCULATING RANDOM WEIGHTS'
            self.weights = np.random.rand(len(input))

        return np.sum(self.weights * input)

    def calculate_output_with_sigmoidal(self, input):

        if len(self.weights) == 0:
            print 'CALCULATING RANDOM WEIGHTS'
            self.weights = np.random.rand(len(input))

        neuron_sum = np.sum(self.weights * input)
        return neuron_sum * (1 - neuron_sum)


class Layer:
    def __init__(self, number_of_perceptrons=0):
        self.perceptrons = []
        for x in range(0, number_of_perceptrons):
            self.perceptrons.append(Perceptron())


class Network:
    def __init__(self, layers=[]):
        self.layers = layers

    def propagate(self):
        return 0

    def calculate_error(self):
        return 0


# Network setup
introLayer = Layer(5)
midLayer = Layer(1)
endLayer = Layer(3)
network = Network([introLayer, midLayer, endLayer])

# Input setup
# TODO : Implement the correct way to get the length of input vector in order to calculate product of weights and input.
dataInput = np.array([[1, 1]])

for layer_index, current_layer in enumerate(network.layers):

    print 'Calculating output for ' + str(layer_index) + ' layer'

    # Calculate output of current layer
    layer_outputs = []
    for index, neuron in enumerate(current_layer.perceptrons):

        print 'Calculating output for ' + str(index) + ' neuron'
        neuron_output = neuron.calculate_output_with_linear(dataInput)

        print 'Neuron weights are: '
        print neuron.weights

        print 'Neuron output is '
        print neuron_output
        neuron.output = neuron_output

        layer_outputs.append(neuron_output)
        print ''

    # Set the output of current layer to the next layer
    dataInput = layer_outputs
