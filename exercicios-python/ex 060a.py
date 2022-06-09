print('---- CÁLCULO DE FATORIAL ----')
num = int(input('Digite um valor: '))
c = num
f = 1
print('\033[34m{}!\033[m = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c-=1
print(f)
