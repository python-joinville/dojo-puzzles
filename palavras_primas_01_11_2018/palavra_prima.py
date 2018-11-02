import string

def palavra_prima(palavra):

    words = list(string.ascii_lowercase)
    soma = sum((words.index(word) + 1) for word in palavra)
    if soma == 11:
        return True    
    
    return !(soma % 2 == 0