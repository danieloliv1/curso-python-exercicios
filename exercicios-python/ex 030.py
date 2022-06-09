n1 = int(input('Digite um número: '))
a = n1 / 2
if a == int(a):
    print('O número {} é par.'.format(n1))
else:
    print('O número {} é ímpar.'.format(n1))
''' Podemos utilizar o a conta {} % 2. Todo número par dividido por 2, o resto da divisão será 0 
e todo número ímpar, o resto da divisão será 1.'''
