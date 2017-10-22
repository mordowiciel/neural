import numpy as np


class Perceptron:

    def __init__(self):
        self.weights = np.random.rand(1, 2)
        self.output = 0

    def calculate_output_with_linear(self, input):
        return np.sum(self.weights * input)

    def calculate_output_with_sigmoidal(self, input):
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



# 1) oblicz output dla kazdego neuronu w warstwie
# 2) wez kazdy output i stworz z niego wektor wejsc
# 3) dla kazdego neuronu w kolejnej warstwie przyporzadkuj powyzsza tablice na wejscie

introLayer = Layer(5)
midLayer = Layer(1)

dataInput = np.array([[1.0, 1.0]])


# 1) Calculate output for every neuron in the layer.
layer_outputs = []
for index, neuron in enumerate(introLayer.perceptrons):

    print 'Calculating output for ' + str(index) + ' neuron'
    print 'Neuron weights are: '
    print neuron.weights

    neuron_output = neuron.calculate_output_with_linear(dataInput)
    print 'Neuron output is '
    print neuron_output
    neuron.output = neuron_output


    layer_outputs.append(neuron_output)
    print ''


print 'Array of outputs of layer is: '
print layer_outputs



