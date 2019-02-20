from converte_num_letra import converte_num_letra

def test_imprime_a():
    resultado = converte_num_letra('2')
    assert resultado == 'a'

def test_imprime_d():
    resultado = converte_num_letra('3')
    assert resultado == 'd'