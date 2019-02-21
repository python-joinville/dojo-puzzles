tabela = {'2': 'a',
          '3':'d', 
          '5':'j',
          '4':'g',
          '6':'m',
          '7':'p',
          '8':'t',
          '9': 'w',
          '0': ' ',
}

def converte_num_letra(digitos):
    palavra = ''
    letra = ''
    sequencia = ''
    for digito in digitos:
        if letra != '' and digito != letra:
            palavra = palavra + tabela[digito]        
        sequencia += digito             
        palavra = palavra + tabela[digito]
    return palavra
