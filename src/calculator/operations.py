"""Basic arithmetic operations for the calculator."""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide the first number by the second and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
