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
