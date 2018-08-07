from ano_bissexto import ano_bissexto


def test_ano_recebe_1600_divisivel_400():
    resultado = ano_bissexto(1600)
    assert resultado
