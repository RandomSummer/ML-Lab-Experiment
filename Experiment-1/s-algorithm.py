import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def find_s_algorithm(data):
    # Initialize the most specific hypothesis
    hypothesis = ['0'] * (len(data[0]) - 1)

    for example in data:
        if example[-1] == 'Yes':  # Consider only positive examples
            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'

    return hypothesis


# Example usage
file_path = 'training_data.csv'
data = read_csv(file_path)
hypothesis = find_s_algorithm(data)
print("The most specific hypothesis is:", hypothesis)
