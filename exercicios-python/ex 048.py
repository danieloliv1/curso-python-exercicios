s = 0
m = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        m += 1
print('A soma dos {} valores solicitados é igual a {}'.format(m, s))
