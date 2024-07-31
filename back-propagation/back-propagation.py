import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Training data
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Initialize weights
input_layer_neurons = inputs.shape[1]
hidden_layer_neurons = 2
output_layer_neurons = 1

hidden_weights = np.random.uniform(
    size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(
    size=(hidden_layer_neurons, output_layer_neurons))
output_bias = np.random.uniform(size=(1, output_layer_neurons))

# Training the neural network
learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):
    # Forward pass
    hidden_layer_activation = np.dot(inputs, hidden_weights)
    hidden_layer_activation += hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    output_layer_activation = np.dot(hidden_layer_output, output_weights)
    output_layer_activation += output_bias
    predicted_output = sigmoid(output_layer_activation)

    # Compute the error
    error = outputs - predicted_output

    # Backward pass
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * \
        sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    output_weights += hidden_layer_output.T.dot(
        d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0,
                          keepdims=True) * learning_rate
    hidden_weights += inputs.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0,
                          keepdims=True) * learning_rate

print("Final hidden weights: ", hidden_weights)
print("Final hidden biases: ", hidden_bias)
print("Final output weights: ", output_weights)
print("Final output biases: ", output_bias)
print("Predicted output: ", predicted_output)
