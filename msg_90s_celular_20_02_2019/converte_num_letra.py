tabela = {'2':'a', 
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
    for digito in digitos:
        palavra = palavra + tabela[digito]
    return palavra
