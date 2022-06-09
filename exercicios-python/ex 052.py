n = int(input('Digite um número: '))
m = 0
for c in range(2, n):
    if n % c == 0:
        print('{}'.format(c), end=' -> ')
        m += 1
if m == 0:
    print('É primo!')
else:
    print('são múltiplos de {}.'.format(n))
    print('Logo, não é primo! Tem {} múltiplos além de 1 e {}.'.format(m, n))
