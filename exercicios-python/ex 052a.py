n = int(input('Digite um número: '))
m = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;31m', end='')
        m += 1
    else:
        print('\033[34m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, m))
if m == 2:
    print('\033[mÉ primo!')
else:
    print('\033[mLogo, não é primo! Tem {} múltiplos além de 1 e ele mesmo.'.format(m))
