tabela = {'2': ['a', 'b', 'c']
        #   '3':'d', 
        #   '5':'j',
        #   '4':'g',
        #   '6':'m',
        #   '7':'p',
        #   '8':'t',
        #   '9': 'w',
        #   '0': ' ',
}

def converte_num_letra(digitos):
    palavra = ''
    letra = ''
    ocorrencia = 0
    for digito in digitos:
        if ocorrencia == 0:
            letra = digito
            palavra = tabela[digito][ocorencia] 
        elif digito == letra:
            palavra = tabela[digito][ocorencia]  
        # palavra = palavra + tabela[digito]
        ocorencia =+ 1
    return palavra
