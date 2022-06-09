inicio = int(input('Início da PA: '))
razao = int(input('Razão da PA: '))
print('Os 10 primeiros termos dessa progressão são:')
for c in range(inicio, inicio + 10 * razao, razao):
    print(c, end=' ')
