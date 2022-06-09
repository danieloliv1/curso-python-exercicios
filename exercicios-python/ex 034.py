salário = float(input('Digite o seu salário: R$'))
if salário >1250:
    novo = salário *1.1
else:
    novo = salário * 1.15
print('Seu salário reajustado será R${:.2f}.'.format(novo))
