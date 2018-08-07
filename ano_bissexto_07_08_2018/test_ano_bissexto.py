from ano_bissexto import ano_bissexto


def test_ano_recebe_1600_eh_bissexto():
    resultado = ano_bissexto(1600)
    assert resultado


def test_ano_recebe_1732_eh_bissexto():
    resultado = ano_bissexto(1732)
    assert resultado


def test_ano_recebe_1742_eh_bissexto():
    resultado = ano_bissexto(1742)
    assert resultado == False


def test_ano_400():
    for i in range(10):
        resultado = ano_bissexto(i*400)
        assert resultado


def test_ano_negativo():
    resultado = ano_bissexto(-400)
    assert resultado
