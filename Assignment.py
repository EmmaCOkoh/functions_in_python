# Question 1

def add_numbers(num1, num2):
    return num1 + num2

# Example usage
result = add_numbers(10, 20)
print("The Sum is:", result)

# Example usage
# Explanation:
# A function add_numbers() is defined with two parameters num1 and num2.
# The function returns their sum using return num1 + num2.
# The function is called with 10 and 20, and the result is printed.


# Question 2

def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
print(is_even(10))  # Output: Even
print(is_even(7))   # Output: Odd

# Explanation:
# The function takes an integer num as input.
# It checks if num % 2 == 0. If True, it returns "Even", otherwise "Odd".
# The function is tested with 10 (even) and 7 (odd).


# Question 3

def greet(name="Guest"):
    print("Hello,", name)

# Example usage
greet("Emmanuel")  # Output: Hello, Emmanuel
greet()         # Output: Hello, Guest

# Explanation:
# The function has a default argument name="Guest".
# If a name is provided, it prints "Hello, name", otherwise, it prints "Hello, Guest".


# Question 4


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
print("Factorial of 5:", factorial(5))  # Output: 120

# Explanation:
# The function recursively calculates factorial.
# If n == 1, it returns 1.
# Otherwise, it returns n * factorial(n - 1).
# Example: factorial(5) = 5 × 4 × 3 × 2 × 1 = 120.
