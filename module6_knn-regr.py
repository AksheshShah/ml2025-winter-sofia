import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def predict(self, query_x):
        if len(self.points) < self.k:
            return "Error: k cannot be greater than the number of data points (N)."

        data = np.array(self.points)  
        x_values = data[:, 0]
        y_values = data[:, 1]

        
        distances = np.abs(x_values - query_x)

        
        k_indices = np.argsort(distances)[:self.k]

        
        k_y_values = y_values[k_indices]
        return np.mean(k_y_values)

def main():
    
    while True:
        try:
            N = int(input("Enter the number of data points (N): "))
            if N <= 0:
                print("N must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    
    while True:
        try:
            k = int(input("Enter the number of neighbors (k): "))
            if k <= 0:
                print("k must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    regressor = KNNRegressor(k)

    
    print(f"Enter {N} (x, y) points:")
    for i in range(N):
        while True:
            try:
                x = float(input(f"Point {i+1} - x: "))
                y = float(input(f"Point {i+1} - y: "))
                regressor.add_point(x, y)
                break
            except ValueError:
                print("Please enter valid real numbers for x and y.")

    
    while True:
        try:
            query_x = float(input("Enter the value of X to predict Y: "))
            break
        except ValueError:
            print("Please enter a valid real number.")

    
    result = regressor.predict(query_x)
    print(f"Predicted Y value: {result}" if isinstance(result, float) else result)

if __name__ == "__main__":
    main()
