import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNModel:
    def __init__(self, k):
        self.k = k
        self.X = []
        self.y = []

    def add_point(self, x_val, y_val):
        self.X.append([x_val])  
        self.y.append(y_val)

    def compute_variance(self):
        return np.var(self.y)

    def predict(self, query_x):
        if len(self.X) < self.k:
            return "Error: k cannot be greater than the number of data points (N)."
        
        model = KNeighborsRegressor(n_neighbors=self.k)
        model.fit(self.X, self.y)
        prediction = model.predict([[query_x]])
        return prediction[0]

def main():
    # Input N
    while True:
        try:
            N = int(input("Enter the number of data points (N): "))
            if N <= 0:
                print("N must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Input k
    while True:
        try:
            k = int(input("Enter the number of neighbors (k): "))
            if k <= 0:
                print("k must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    model = KNNModel(k)


    print(f"Enter {N} (x, y) data points:")
    for i in range(N):
        while True:
            try:
                x = float(input(f"Point {i+1} - x: "))
                y = float(input(f"Point {i+1} - y: "))
                model.add_point(x, y)
                break
            except ValueError:
                print("Invalid input. Please enter real numbers.")


    while True:
        try:
            query_x = float(input("Enter the value of X to predict Y: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number.")


    result = model.predict(query_x)
    if isinstance(result, str):
        print(result)
    else:
        variance = model.compute_variance()
        print(f"Predicted Y value for X = {query_x}: {result}")
        print(f"Variance of Y in training data: {variance}")

if __name__ == "__main__":
    main()
