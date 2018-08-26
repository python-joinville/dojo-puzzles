

def ano_bissexto(ano):
    if type(ano) is int and ano >= 0:
        return bool((eh_divisivel(ano, 4) and
                        not eh_divisivel(ano, 100)) or
                        eh_divisivel(ano, 400))
    return False


def eh_divisivel(numero, outro_numero):
    return not numero % outro_numero
