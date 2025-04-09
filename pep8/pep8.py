import os
import sys
from typing import List



class Calculator:
    """A simple calculator class. Where we can add and subtract numbers."""

    def add(self, a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Subtract two numbers."""
        return a - b


def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}"


def calculate_sum(numbers: List[int]) -> int:
    """Calculate the sum of a list of numbers."""
    return sum(numbers)


if __name__ == "__main__":
    # Example usage
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))

    print(greet("Mamun"))

    numbers = [1, 2, 3, 4, 5]
    print(calculate_sum(numbers))