from ano_bissexto import ano_bissexto
import pytest


@pytest.mark.parametrize("ano,esperado", [
    (1600, True),
    (1732, True),
    (1888, True),
    (1944, True),
    (2008, True),
    (1742, False),
    (1889, False),
    (1951, False),
    (2011, False),
    (1500, False),
    (-1, False),
    (-4, False),
    (-400, False),
])
def test_ano_eh_bissexto(ano, esperado):
    resultado = ano_bissexto(ano)
    assert esperado == resultado


def test_ano_400():
    for i in range(10):
        resultado = ano_bissexto(i*400)
        assert resultado
