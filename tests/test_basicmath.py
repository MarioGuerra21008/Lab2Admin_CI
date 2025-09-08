import pytest
from basicmathlib.basicmath import square, factorial, is_prime

# ---------------- square ----------------
def test_square_happy_paths():
    assert square(3) == 9
    assert square(-2.5) == 6.25

def test_square_errors():
    with pytest.raises(TypeError):
        square("3")  # not numeric
    with pytest.raises(ValueError):
        square(float("inf"))

# ---------------- factorial ----------------
def test_factorial_happy_paths():
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_factorial_errors():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(3.5)  # must be integer

# ---------------- is_prime ----------------
def test_is_prime_happy_paths():
    assert is_prime(2) is True
    assert is_prime(15) is False  # composite

def test_is_prime_edges_and_errors():
    assert is_prime(1) is False
    assert is_prime(0) is False
    with pytest.raises(TypeError):
        is_prime(7.0)  # non-integer