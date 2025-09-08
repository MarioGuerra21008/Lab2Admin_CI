from __future__ import annotations
from math import isfinite

__all__ = ["square", "factorial", "is_prime", "gcd", "lcm"]

def square(n: int | float) -> int | float: # Returns the square of a number.
    return n * n


def factorial(n: int) -> int: # Factorial of a number.
    if n < 0:
        raise ValueError("n must be >= 0 for factorial.")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


def is_prime(n: int) -> bool: # Evaluates if a number is prime or not.
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def gcd(a: int, b: int) -> int: # Greatest Common Divisor.
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int: # Least Common Multiple.
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)