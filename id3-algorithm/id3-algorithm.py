import csv
import math


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def entropy(data):
    total = len(data)
    positive = sum(1 for row in data if row[-1] == 'Yes')
    negative = total - positive
    if positive == 0 or negative == 0:
        return 0
    p_positive = positive / total
    p_negative = negative / total
    return -p_positive * math.log2(p_positive) - p_negative * math.log2(p_negative)


def information_gain(data, attribute_index):
    total_entropy = entropy(data)
    values = set(row[attribute_index] for row in data)
    weighted_entropy = sum((sum(1 for row in data if row[attribute_index] == value) / len(
        data)) * entropy([row for row in data if row[attribute_index] == value]) for value in values)
    return total_entropy - weighted_entropy


def id3(data, attributes):
    if all(row[-1] == 'Yes' for row in data):
        return 'Yes'
    if all(row[-1] == 'No' for row in data):
        return 'No'
    if not attributes:
        return max(set(row[-1] for row in data), key=lambda label: sum(1 for row in data if row[-1] == label))

    best_attribute = max(
        attributes, key=lambda attr: information_gain(data, attr))
    tree = {best_attribute: {}}
    values = set(row[best_attribute] for row in data)
    for value in values:
        subset = [row for row in data if row[best_attribute] == value]
        subtree = id3(
            subset, [attr for attr in attributes if attr != best_attribute])
        tree[best_attribute][value] = subtree
    return tree


# Example usage
file_path = 'training_data.csv'
data = read_csv(file_path)
attributes = list(range(len(data[0]) - 1))
decision_tree = id3(data, attributes)
print("The decision tree is:", decision_tree)
