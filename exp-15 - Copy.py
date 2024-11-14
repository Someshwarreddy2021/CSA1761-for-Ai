import numpy as np

# Function to calculate Gini Impurity
def gini_impurity(y):
    classes, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    gini = 1 - np.sum(probs ** 2)
    return gini

# Function to perform a split based on a feature and a threshold
def best_split(X, y):
    best_gini = float("inf")
    best_split_value = None
    best_left_y = None
    best_right_y = None
    best_left_X = None
    best_right_X = None
    n_features = X.shape[1]

    # Iterate over all features and their unique values
    for feature_idx in range(n_features):
        feature_values = np.unique(X[:, feature_idx])
        for threshold in feature_values:
            left_mask = X[:, feature_idx] <= threshold
            right_mask = ~left_mask

            left_y = y[left_mask]
            right_y = y[right_mask]

            # Skip if any of the branches have no data
            if len(left_y) == 0 or len(right_y) == 0:
                continue

            gini = (len(left_y) / len(y)) * gini_impurity(left_y) + (len(right_y) / len(y)) * gini_impurity(right_y)

            if gini < best_gini:
                best_gini = gini
                best_split_value = (feature_idx, threshold)
                best_left_y = left_y
                best_right_y = right_y
                best_left_X = X[left_mask]
                best_right_X = X[right_mask]

    return best_split_value, best_left_X, best_right_X, best_left_y, best_right_y

# Function to create a decision tree recursively
def build_tree(X, y, max_depth=None, min_size=1, depth=0):
    if len(np.unique(y)) == 1:  # Pure node
        return np.unique(y)[0]

    if max_depth is not None and depth >= max_depth:  # Max depth reached
        return np.argmax(np.bincount(y))  # Return the majority class

    if len(y) <= min_size:  # Minimum size reached
        return np.argmax(np.bincount(y))  # Return the majority class

    split, left_X, right_X, left_y, right_y = best_split(X, y)

    if split is None:  # No further split is possible
        return np.argmax(np.bincount(y))

    left_branch = build_tree(left_X, left_y, max_depth, min_size, depth + 1)
    right_branch = build_tree(right_X, right_y, max_depth, min_size, depth + 1)

    return (split, left_branch, right_branch)

# Function to predict using the decision tree
def predict_tree(node, x):
    if not isinstance(node, tuple):  # Leaf node
        return node

    feature_idx, threshold = node[0]
    if x[feature_idx] <= threshold:
        return predict_tree(node[1], x)
    else:
        return predict_tree(node[2], x)

# Function to fit the decision tree
def fit(X, y, max_depth=None, min_size=1):
    return build_tree(X, y, max_depth, min_size)

# Function to predict a set of examples
def predict(tree, X):
    return [predict_tree(tree, x) for x in X]

# Example usage:
if __name__ == "__main__":
    # Toy dataset
    X = np.array([[2, 3],
                  [1, 2],
                  [3, 1],
                  [2, 4],
                  [3, 3]])
    y = np.array([0, 0, 1, 1, 0])  # Binary classification

    # Train the decision tree
    tree = fit(X, y, max_depth=3)

    # Predict on new data
    predictions = predict(tree, X)
    
    print("Predictions:", predictions)
