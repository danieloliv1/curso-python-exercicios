frase = str(input('Digite algo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('O inverso de {} é {}.'.format(junto, inverso))
    print('É um palíndromo!')
else:
    print('O inverso de {} é {}.'.format(junto, inverso))
    print('Não é um palíndromo')
