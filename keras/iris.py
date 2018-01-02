#!/opt/anaconda2/envs/datascience/bin/python2.7

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn import datasets

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

def baseline_model():
    network_model = Sequential()
    network_model.add(Dense(8, input_dim=4, activation='relu'))
    network_model.add(Dense(3, activation='softmax'))
    network_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return network_model

iris_dataset = datasets.load_iris()

X = iris_dataset.data
Y = iris_dataset.target
dummy_y = np_utils.to_categorical(Y)

print dummy_y

# estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5)
# kfold = KFold(n_splits=2, shuffle=True, random_state=5)
#
# results = cross_val_score(estimator, X, dummy_y, cv=kfold)
# print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
