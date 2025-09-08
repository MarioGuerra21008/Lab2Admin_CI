import pytest
from basicmathlib.basicmath import square

# ---------------- square ----------------
def test_square_happy_paths():
    assert square(3) == 9
    assert square(-2.5) == 6.25

def test_square_errors():
    with pytest.raises(TypeError):
        square("3")  # not numeric
    with pytest.raises(ValueError):
        square(float("inf"))