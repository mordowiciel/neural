#!/opt/anaconda2/envs/datascience/bin/python2.7

from keras.models import Sequential
from keras.layers import Dense
import numpy


dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")

training_set = dataset[0::2]
test_set = dataset[1::2]

x_train = training_set[:, 0:8]
y_train = training_set[:, 8]

x_test = test_set[:, 0:8]
y_test = test_set[:, 8]

network_model = Sequential()
network_model.add(Dense(12, input_dim=8, activation='relu'))
network_model.add(Dense(8, activation='relu'))
network_model.add(Dense(1, activation='sigmoid'))

network_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
network_model.fit(x_train, y_train, epochs=150, batch_size=1)

scores = network_model.evaluate(x_test, y_test)
print("\n%s: %.2f%%" % (network_model.metrics_names[1], scores[1]*100))