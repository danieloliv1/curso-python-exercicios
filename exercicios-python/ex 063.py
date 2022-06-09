print('\033[1;34m---- Sequência de Fibonacci ----\033[m')
n = int(input('Quantos termos deseja ver? '))
fn1 = 0
fn2 = 1
print('{} > {}'.format(fn1,  fn2), end='')
c = 3
while c <= n:
    fn3 = fn1 + fn2
    print(' > {}'.format(fn3), end='')
    fn1 = fn2
    fn2 = fn3
    c += 1
