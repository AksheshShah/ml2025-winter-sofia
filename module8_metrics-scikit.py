import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Get number of points from user
    while True:
        try:
            n = int(input("Enter the number of points (N): "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Initialize numpy arrays for storing the data
    x_values = np.zeros(n, dtype=int)  # Ground truth labels
    y_values = np.zeros(n, dtype=int)  # Predicted labels
    
    # Read N (x, y) points from user
    print(f"\nPlease enter {n} points (x, y) where x is ground truth and y is predicted:")
    print("Both x and y should be either 0 or 1")
    
    for i in range(n):
        print(f"\nPoint {i + 1}:")
        
        # Read x value (ground truth)
        while True:
            try:
                x = int(input("Enter x (ground truth - 0 or 1): "))
                if x in [0, 1]:
                    x_values[i] = x
                    break
                else:
                    print("x must be either 0 or 1.")
            except ValueError:
                print("Please enter a valid integer (0 or 1).")
        
        # Read y value (predicted)
        while True:
            try:
                y = int(input("Enter y (predicted - 0 or 1): "))
                if y in [0, 1]:
                    y_values[i] = y
                    break
                else:
                    print("y must be either 0 or 1.")
            except ValueError:
                print("Please enter a valid integer (0 or 1).")
    
    # Display the collected data
    print(f"\nCollected data:")
    print(f"Ground truth (x): {x_values}")
    print(f"Predicted (y):    {y_values}")
    
    # Calculate Precision and Recall using scikit-learn
    try:
        precision = precision_score(x_values, y_values, zero_division=0)
        recall = recall_score(x_values, y_values, zero_division=0)
        
        print(f"\nResults:")
        print(f"Precision: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        
        # Optional: Display additional information
        print(f"\nAdditional information:")
        
        # Calculate confusion matrix components manually for explanation
        tp = np.sum((x_values == 1) & (y_values == 1))  # True Positives
        fp = np.sum((x_values == 0) & (y_values == 1))  # False Positives
        fn = np.sum((x_values == 1) & (y_values == 0))  # False Negatives
        tn = np.sum((x_values == 0) & (y_values == 0))  # True Negatives
        
        print(f"True Positives (TP): {tp}")
        print(f"False Positives (FP): {fp}")
        print(f"False Negatives (FN): {fn}")
        print(f"True Negatives (TN): {tn}")
        
        # Show formulas
        if tp + fp > 0:
            print(f"Precision = TP / (TP + FP) = {tp} / ({tp} + {fp}) = {precision:.4f}")
        else:
            print(f"Precision = TP / (TP + FP) = {tp} / 0 = 0.0000 (no positive predictions)")
            
        if tp + fn > 0:
            print(f"Recall = TP / (TP + FN) = {tp} / ({tp} + {fn}) = {recall:.4f}")
        else:
            print(f"Recall = TP / (TP + FN) = {tp} / 0 = 0.0000 (no positive ground truth)")
            
    except Exception as e:
        print(f"Error calculating metrics: {e}")

if __name__ == "__main__":
    main()