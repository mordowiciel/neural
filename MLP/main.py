from layer import *
from network import *

# Input setup
dataInput = np.array([1, 1]).transpose()
dataOutput = np.array([2, 2])

# Network setup
introLayer = Layer(3)
midLayer = Layer(1)
endLayer = Layer(2)
network = Network([introLayer, midLayer, endLayer])

# Network learning
network.propagate(dataInput)
network.calculate_error(dataOutput)

for layer in network.layers:

    for neuron in layer.perceptrons:
        print neuron.error_value

