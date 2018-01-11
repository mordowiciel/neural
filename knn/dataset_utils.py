import matplotlib.pyplot as plt
import numpy as np
import itertools
import os.path


def divide_k_cross(data, test_index):

    # Calculate the dataset split.
    split = len(data) / 3

    k_data = [data[:split], data[split:2 * split], data[2 * split:]]
    test_data = k_data[test_index]

    k_data.pop(test_index)

    training_data = k_data
    training_data = k_data[0] + k_data[1]

    return training_data, test_data


def get_classification_labels(data_matrix):
    class_labels = set([])
    for row in data_matrix:
        class_labels.add(row[-1])
    return class_labels


def convert_to_point_label_tuple(data_matrix):

    data_tuples = []
    class_labels = set([])
    for row in data_matrix:
        row_tuple = (row[:-1], row[-1])
        data_tuples.append(row_tuple)

    return data_tuples


def plot_confusion_matrix(number_of_neighbours,
                          metric,
                          dataset_name,
                          is_normalized,
                          cm,
                          classes,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    print(cm)

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

# plt.show()
    dataset_name = dataset_name.split("/")[1].split(".")[0]
    normalized_str = ""
    if(is_normalized):
        normalized_str = "_norm"

    plot_name = str(number_of_neighbours) + "N" + "_" + metric + "_" + dataset_name + normalized_str

    plt.savefig("plots" + "/" + dataset_name + "/" + plot_name)
