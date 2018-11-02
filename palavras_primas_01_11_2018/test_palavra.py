from palavra_prima import palavra_prima

def test_palavra_a_retorna_true():
    esperado = palavra_prima('a')
    assert esperado

def test_palavra_ab_retorna_true():
    esperado = palavra_prima('ab')
    assert esperado

def test_palabra_abc_retorna_false():
    esperado = palavra_prima('abc')
    assert not esperado

def test_palabra_d_retorna_false():
    esperado = palavra_prima('d')
    assert not esperado

def test_palavra_af_retorna_true():
    esperado = palavra_prima('af')
    assert esperado