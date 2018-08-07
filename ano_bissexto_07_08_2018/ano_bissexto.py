
def ano_bissexto(ano):
    if type(ano) is not int:
        return False

    if ano < 0:
        return False
    elif ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False
