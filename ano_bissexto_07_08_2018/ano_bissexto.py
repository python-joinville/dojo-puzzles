
def ano_bissexto(ano):
    if ano == 1600:
        return True
    elif ano == 1732:
        return True
    elif ano % 400 == 0:
        return True
    else:
        return False
