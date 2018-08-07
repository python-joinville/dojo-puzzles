

def ano_bissexto(ano):
    if type(ano) is int:
        if ano < 0:
            return False
        # elif ano % 400 == 0:
        #     return True
        # elif ano % 100 == 0:
        #     return False
        # elif ano % 4 == 0:
        #     return True
        # else:
        #     return False
        return not bool(ano%400 or (ano%4 and not ano%100))
    return False
