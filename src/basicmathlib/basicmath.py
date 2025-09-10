from __future__ import annotations
from math import isfinite

__all__ = ["square", "factorial", "is_prime", "gcd", "lcm"]

def ensure_number(x):
    if not isinstance(x, (int, float)):
        raise TypeError("A number expected (int or float).")
    if isinstance(x, float) and not isfinite(x):
        raise ValueError("Number must be finite.")
    return x


def ensure_int(x, name="n"):
    if not isinstance(x, int):
        raise TypeError(f"{name} must be an integer.")
    return x

def square(n: int | float) -> int | float: # Returns the square of a number.
    ensure_number(n)
    return n * n


def factorial(n: int) -> int: # Factorial of a number.
    ensure_int(n, "n")
    if n < 0:
        raise ValueError("n must be >= 0 for factorial.")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return 1


def is_prime(n: int) -> bool: # Evaluates if a number is prime or not.
    ensure_int(n, "n")
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
    ensure_int(a, "a")
    ensure_int(b, "b")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int: # Least Common Multiple.
    ensure_int(a, "a")
    ensure_int(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)