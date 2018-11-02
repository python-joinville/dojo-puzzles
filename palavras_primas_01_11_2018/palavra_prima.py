import string

def palavra_prima(palavra):
    words = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6
    }
    soma = sum(words.get(word) for word in palavra)
    return soma in [1,3,5,7]