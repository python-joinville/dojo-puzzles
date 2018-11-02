import string

def palavra_prima(palavra):

    words = list(string.ascii_lowercase)
    soma = sum((words.index(word) + 1) for word in palavra)
    if soma <= 3:
        return True
    if soma % 2 == 0 or soma % 3 == 0:
        return False   
    return True
    