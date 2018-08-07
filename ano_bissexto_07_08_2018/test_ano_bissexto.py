from ano_bissexto import ano_bissexto
import pytest


@pytest.mark.parametrize("ano,esperado", [
    (1600, True),
    (1732, True),
    (1888, True),
    (1742, False),
    (1889, False),
    (1500, False),
])
def test_ano_eh_bissexto(ano, esperado):
    resultado = ano_bissexto(ano)
    assert esperado == resultado


def test_ano_400():
    for i in range(10):
        resultado = ano_bissexto(i*400)
        assert resultado


def test_ano_negativo():
    resultado = ano_bissexto(-400)
    assert resultado
