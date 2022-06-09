frase = str(input('Digite algo: ')).strip()
if frase.replace(' ', '').upper() == frase[::-1].replace(' ', '').upper():
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')
