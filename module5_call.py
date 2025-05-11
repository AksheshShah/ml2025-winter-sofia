from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    while True:
        try:
            N = int(input("Enter a positive integer (N): "))
            if N <= 0:
                print("N must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                processor.insert_number(num)
                break
            except ValueError:
                print("Please enter a valid integer.")

    while True:
        try:
            X = int(input("Enter the number to search (X): "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    result = processor.search_number(X)
    print(result)

if __name__ == "__main__":
    main()
