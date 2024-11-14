import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid function (for backpropagation)
def sigmoid_derivative(x):
    return x * (1 - x)

# Mean Squared Error Loss function
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Feedforward Neural Network class
class FeedforwardNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.1):
        # Initialize weights and biases
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Randomly initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.random.rand(1, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.random.rand(1, self.output_size)

    def forward(self, X):
        # Forward pass through the network
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)

        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)

        return self.final_output

    def backward(self, X, y, output):
        # Backward pass (Gradient Descent + Backpropagation)
        error = y - output

        # Output layer error
        output_error = error * sigmoid_derivative(output)
        
        # Hidden layer error
        hidden_error = output_error.dot(self.weights_hidden_output.T) * sigmoid_derivative(self.hidden_output)

        # Update weights and biases using gradient descent
        self.weights_hidden_output += self.hidden_output.T.dot(output_error) * self.learning_rate
        self.bias_output += np.sum(output_error, axis=0, keepdims=True) * self.learning_rate

        self.weights_input_hidden += X.T.dot(hidden_error) * self.learning_rate
        self.bias_hidden += np.sum(hidden_error, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs=10000):
        # Training the model using backpropagation
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)

            # Optionally print the loss every 1000 iterations
            if epoch % 1000 == 0:
                loss = mse_loss(y, output)
                print(f'Epoch {epoch}, Loss: {loss}')

    def predict(self, X):
        # Predict using the trained model
        return self.forward(X)

# Example Usage
if __name__ == "__main__":
    # Input data (X) and output data (y)
    # XOR Problem (for example)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input features
    y = np.array([[0], [1], [1], [0]])  # Output labels

    # Define the neural network with 2 input neurons, 2 hidden neurons, and 1 output neuron
    nn = FeedforwardNN(input_size=2, hidden_size=2, output_size=1, learning_rate=0.1)

    # Train the model
    nn.train(X, y, epochs=10000)

    # Make predictions on the training data
    predictions = nn.predict(X)
    print("\nPredictions after training:")
    print(predictions)
