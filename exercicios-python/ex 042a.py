print('-=-' * 12)
print('\033[1;34mAnalisador de Triângulos.\033[m')
print('-=-' * 12)
a = float(input('Valor de A: '))
b = float(input('Valor de B: '))
c = float(input('Valor de C: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a == b or a == c or b == c:
        tipo = 'ISÓCELES'
    elif a != b != c != a:
        tipo = 'ESCALENO'
    print('Os seguimentos acima podem formar um triângulo {}.'.format(tipo))
else:
    print('Os seguimentos acima NÃO podem formar um triângulo.')
