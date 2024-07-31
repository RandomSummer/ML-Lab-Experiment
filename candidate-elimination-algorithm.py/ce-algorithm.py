import csv


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def candidate_elimination(data):
    # Initialize the most specific hypothesis (S) and the most general hypothesis (G)
    S = ['0'] * (len(data[0]) - 1)
    G = [['?'] * (len(data[0]) - 1)]

    for example in data:
        if example[-1] == 'Yes':  # Positive example
            for i in range(len(S)):
                if S[i] == '0':
                    S[i] = example[i]
                elif S[i] != example[i]:
                    S[i] = '?'
            G = [g for g in G if all(
                g[i] == '?' or g[i] == example[i] for i in range(len(g)))]
        else:  # Negative example
            G_new = []
            for g in G:
                for i in range(len(g)):
                    if g[i] == '?':
                        for value in set([ex[i] for ex in data if ex[-1] == 'Yes']):
                            if value != example[i]:
                                g_new = g[:]
                                g_new[i] = value
                                G_new.append(g_new)
            G = G_new

    return S, G


# Example usage
file_path = 'training_data.csv'
data = read_csv(file_path)
S, G = candidate_elimination(data)
print("The most specific hypothesis is:", S)
print("The set of all general hypotheses is:", G)
