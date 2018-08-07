from ano_bissexto import ano_bissexto


def test_ano_recebe_1600_eh_bissexto():
    resultado = ano_bissexto(1600)
    assert resultado


def test_ano_recebe_1732_eh_bissexto():
    resultado = ano_bissexto(1732)
    assert resultado
