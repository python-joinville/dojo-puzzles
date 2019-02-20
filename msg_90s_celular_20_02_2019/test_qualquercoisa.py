from converte_num_letra import converte_num_letra
import pytest

@pytest.mark.parametrize("digito,expected", [
    ('2', 'a'),
    ('3', 'd'),
    ('4', 'g'),
    ('5', 'j'),
    ('6', 'm'),
    ('7', 'p'),
    ('8', 't'),    
    ('9', 'w'),
    ('0', ' '),
])
def test_converte_num_digito(digito, expected):
    resultado = converte_num_letra(digito)
    assert resultado == expected

