from perceptron import *


class Layer:

    def __init__(self, number_of_perceptrons=0):

        self.perceptrons = []
        for x in range(0, number_of_perceptrons):
            self.perceptrons.append(Perceptron())
