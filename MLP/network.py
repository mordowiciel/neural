class Network:

    def __init__(self, layers=[]):
        self.layers = layers

    def propagate(self, dataInput):

        for layer_index, current_layer in enumerate(self.layers):

            layer_outputs = []
            print 'Calculating output for ' + str(layer_index) + ' layer'

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

    def calculate_error(self):
        return 0
