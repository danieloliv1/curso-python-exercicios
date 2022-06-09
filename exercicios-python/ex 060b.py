print('---- CÁLCULO DE FATORIAL ----')
num = int(input('Digite um valor: '))
c = num
f = 1
print('\033[34m{}!\033[m = '.format(num), end='')
for c in range(num, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)
