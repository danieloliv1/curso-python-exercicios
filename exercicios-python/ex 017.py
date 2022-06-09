from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
print('O resultado da hipotenusa é igual a {:.2f}'.format(hypot(co, ca)))
