from converte_num_letra import converte_num_letra
import pytest

@pytest.mark.parametrize("digito,expected", [
    ("2", 'a'),
    
])
def test_eval(digito, expected):
    resultado = converte_num_letra(digito)
    assert resultado == expected

def test_imprime_a():
    resultado = converte_num_letra('2')
    assert resultado == 'a'

def test_imprime_d():
    resultado = converte_num_letra('3')
    assert resultado == 'd'

def test_imprime_j():
    assert converte_num_letra('5') == 'j'

def test_imprime_g():
    assert converte_num_letra('4') == 'g'

def test_imprime_m():
    assert converte_num_letra('6') == 'm'

