from layer import *
from network import *

# Input setup
dataInput = np.array([1, 1]).transpose()

# Network setup
introLayer = Layer(3)
midLayer = Layer(1)
endLayer = Layer(2)
network = Network([introLayer, midLayer, endLayer])

# Network learning
network.propagate(dataInput)
