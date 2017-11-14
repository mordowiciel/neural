class Network:
    def __init__(self, layers=[]):
        self.layers = layers

    def propagate(self, data_input):

        for layer_index, current_layer in enumerate(self.layers):

            layer_outputs = []
            print 'Calculating output for ' + str(layer_index) + ' layer'

            for index, neuron in enumerate(current_layer.perceptrons):
                print 'Calculating output for ' + str(index) + ' neuron'
                neuron_output = neuron.calculate_output_with_sigmoidal(data_input)

                print 'Neuron weights are: '
                print neuron.weights

                print 'Neuron output is '
                print neuron_output
                neuron.output = neuron_output

                layer_outputs.append(neuron_output)
                print ''

            # Set the output of current layer to the next layer
            data_input = layer_outputs

    def calculate_error(self, expected_output_values):

        # Create input-output pairs
        expected_output_pairs = dict()
        if len(expected_output_values) == len(self.layers[-1].perceptrons):
            expected_output_pairs = dict(zip(self.layers[-1].perceptrons, expected_output_values))

        for layer_index, current_layer in reversed(list(enumerate(self.layers))):

            for current_neuron in current_layer.perceptrons:

                # Every layer
                if layer_index != len(self.layers) - 1:

                    next_layer = self.layers[layer_index + 1]
                    error_sum = 0
                    for next_neuron in next_layer.perceptrons:
                            error_sum += current_neuron.output * next_neuron.error_value

                    current_neuron.error_value = error_sum

                # Last layer case
                else:
                    current_neuron.error_value = current_neuron.output - expected_output_pairs[current_neuron]
