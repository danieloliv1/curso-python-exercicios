n = int(input('Ditige um número (999 para PARAR): '))
c = soma = 0
while n != 999:
    soma += n
    n = int(input('Ditige um número (999 para PARAR): '))
    c += 1
print('Foram digitados {} números e a soma entre eles foi {}.'.format(c, soma))
