import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# --- Step 1: Read training data ---
N = int(input("Enter the number of training samples (N): "))
print("Enter the training data pairs (x y):")

train_data = []
train_labels = []

for _ in range(N):
    x = float(input("  x: "))
    y = int(input("  y: "))
    train_data.append(x)
    train_labels.append(y)

# Convert to numpy arrays and reshape features to match scikit-learn expectations
X_train = np.array(train_data).reshape(-1, 1)
y_train = np.array(train_labels)

# --- Step 2: Read test data ---
M = int(input("Enter the number of test samples (M): "))
print("Enter the test data pairs (x y):")

test_data = []
test_labels = []

for _ in range(M):
    x = float(input("  x: "))
    y = int(input("  y: "))
    test_data.append(x)
    test_labels.append(y)

X_test = np.array(test_data).reshape(-1, 1)
y_test = np.array(test_labels)

# --- Step 3: Try k from 1 to 10 and compute test accuracy ---
best_k = 1
best_accuracy = 0.0

for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    predictions = knn.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    
    if acc > best_accuracy:
        best_accuracy = acc
        best_k = k

# --- Step 4: Output the result ---
print(f"\nBest k: {best_k}")
print(f"Test accuracy: {best_accuracy:.4f}")
