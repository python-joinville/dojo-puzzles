from palavra_prima import palavra_prima
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("a", True),
    ("ab", True),
    ("abc", False),
    ("d", False),
    ("af", True),
    ("fe", True),
    ("xyyy", False),
])
def test_palavra(test_input, expected):
    esperado = palavra_prima(test_input)
    assert esperado == expected