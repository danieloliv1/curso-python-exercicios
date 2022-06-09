from time import sleep
print('{:=^40}'.format('\033[1;33m LOJAS LEVEL \033[m'))
compras = float(input('Qual o valor das compras? R$'))
print('''Selecione a forma de pagamento.
(1) à vista no dinheiro ou cheque.
(2) à vistã no cartão de crédito ou débito.
(3) em 2x no cartão de crédito.
(4) em 3x ou mais no cartão de crédito.''')
pagamento = int(input('Digite aqui sua opção: '))
if pagamento == 1:
    print('''Sua compra teve um desconto de 10% com essa forma de pagamento.
    Total = R${:.2f}.'''.format(compras * 0.90))
elif pagamento == 2:
    print('''Sua compra teve um desconto de 5% com essa forma de pagamento.
    Total = R${:.2f}.'''.format(compras * 0.95))
elif pagamento == 3:
    print('Total da compra R${:.2f} ou 2x de {:.2f}'.format(compras, compras / 2))
elif pagamento == 4:
    print('Essa opção implicará em juros.')
    sleep(1)
    print(' 3 x R${:.2f}'.format(compras * 1.02 / 3))
    print(' 4 x R${:.2f}'.format(compras * 1.04 / 4))
    print(' 5 x R${:.2f}'.format(compras * 1.06 / 5))
    print(' 6 x R${:.2f}'.format(compras * 1.08 / 6))
    print(' 7 x R${:.2f}'.format(compras * 1.10 / 7))
    print(' 8 x R${:.2f}'.format(compras * 1.12 / 8))
    print(' 9 x R${:.2f}'.format(compras * 1.14 / 9))
    print('10 x R${:.2f}'.format(compras * 1.16 / 10))
    print('11 x R${:.2f}'.format(compras * 1.18 / 11))
    print('12 x R${:.2f}'.format(compras * 1.20 / 12))
    parcela = int(input('Em quantas vezes deseja parcelar? '))
    if parcela == 3:
        total = compras * 1.02
    elif parcela == 4:
        total = compras * 1.04
    elif parcela == 5:
        total = compras * 1.06
    elif parcela == 6:
        total = compras * 1.08
    elif parcela == 7:
        total = compras * 1.10
    elif parcela == 8:
        total = compras * 1.12
    elif parcela == 9:
        total = compras * 1.14
    elif parcela == 10:
        total = compras * 1.16
    elif parcela == 11:
        total = compras * 1.18
    elif parcela == 12:
        total = compras * 1.20
    else:
        print('Opção inválida.')
    print('Total = R${:.2f}.'.format(total))
else:
    print('Opção inválida!')
