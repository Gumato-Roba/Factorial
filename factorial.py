def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            raise ValueError("Input must be a positive integer.")
        break
    except ValueError as b:
        print(b)

print(f"The factorial of {n} is {calculate_factorial(n)}")