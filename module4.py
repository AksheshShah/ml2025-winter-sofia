# Ask the user for a positive integer N
N = int(input("Enter a positive integer N: "))

# Print the entered value
print("You entered:", N)

# Read N numbers one by one
numbers = []
for i in range(N):
    num = int(input("Enter number: "))
    numbers.append(num)

# Print the list of numbers entered
print("You entered:", numbers)

# Ask the user for input X
X = int(input("Enter the number to search for (X): "))

# Search for X and print the result
if X in numbers:
    index = numbers.index(X) + 1  # Convert to 1-based index
    print(index)
else:
    print("-1")
