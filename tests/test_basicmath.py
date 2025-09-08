import pytest
from basicmathlib.basicmath import square, factorial

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
