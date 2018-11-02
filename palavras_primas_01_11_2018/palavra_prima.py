import string

def palavra_prima(palavra):

    words = list(string.ascii_lowercase)
    soma = sum((words.index(word) + 1) for word in palavra)
    return soma in [1,3,5,7]