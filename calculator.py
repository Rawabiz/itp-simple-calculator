print("This calculator will show you results for different calculations on values you enter")

x = float(input("\nKindly Enter the first value: "))
y = float(input("\nKindly Enter the second value: "))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Can't do division by zero"
    return x / y

def multiply(x, y):
    return x * y

def square(x):
    return x ** 2

def power(x, y):
    return x ** y

def sqrt(x):
    return x ** 0.5

print("\nResults of calculations:")
print(f"Addition: {add(x, y)}")
print(f"Subtraction: {subtract(x, y)}")
print(f"Multiplication: {multiply(x, y)}")
print(f"Division: {divide(x, y)}")
print(f"Square of first number: {square(x)}")
print(f"Square root of first number: {sqrt(x)}")
print(f"{x} to the power of {y}: {power(x, y)}")

def test_calculator(x, y):
    print("\nRunning tests...")

    assert add(x, y) == x + y
    assert subtract(x, y) == x - y
    if y != 0:
        assert divide(x, y) == x / y
    else:
        assert divide(x, y) == "Can't do division by zero"
    assert multiply(x, y) == x * y
    assert square(x) == x ** 2
    assert power(x, y) == x ** y
    assert sqrt(x) == x ** 0.5

    print("All tests passed!")

if __name__ == "__main__":
    test_calculator(x, y)
