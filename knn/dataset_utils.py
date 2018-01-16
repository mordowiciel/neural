import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
import os.path


def convert_to_data_tuple(data, labels, train_index, test_index):
    data_train, data_test = data[train_index], data[test_index]
    labels_train, labels_test = labels[train_index], labels[test_index]

    training_data = []
    for i in range(0, len(data_train)):
        train_tuple = (data_train[i], labels_train[i])
        training_data.append(train_tuple)

    test_data = []
    for i in range(0, len(data_test)):
        test_tuple = (data_test[i], labels_test[i])
        test_data.append(test_tuple)

    return training_data, test_data


def create_confusion_matrix(knn, test_data):

    true_arr = []
    predicted_arr = []

    for point in test_data:
        classification_label = knn.classify_point(point[0])
        true_arr.append(point[1])
        predicted_arr.append(classification_label)

        # if(point[1] == classification_label):
        #     properly_classified += 1

    cm = confusion_matrix(true_arr, predicted_arr)
    return cm


def print_cm_info(cm, labels):
    for index, class_label in enumerate(set(labels)):
        row_sum = np.sum(cm[index, :]) - cm[index][index]
        col_sum = np.sum(cm[:, index]) - cm[index][index]
        print "False negatives for", class_label, str(row_sum)
        print "False positives for", class_label, str(col_sum)

    print cm


def plot_confusion_matrix(number_of_neighbours,
                          metric,
                          dataset_name,
                          is_normalized,
                          cm,
                          classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):

    print "Inside plot_confusion_matrix"
    print cm

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout(pad=1.75)
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    dataset_name = dataset_name.split("/")[1].split(".")[0]
    normalized_str = ""
    if(is_normalized):
        normalized_str = "_norm"

    plot_name = str(number_of_neighbours) + "N" + "_" + metric + "_" + dataset_name + normalized_str
    plt.savefig("plots" + "/" + dataset_name + "/" + plot_name)
