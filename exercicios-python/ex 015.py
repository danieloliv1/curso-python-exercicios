dias = int(input('Digite a quantidade de dias que o veículo foi alugado: '))
km = float(input('Digite a quilometragem rodada: '))
custodias = dias * 60
custokm = km * 0.15
print('O valor das diárias ficou em R${:.2f} mais R${:.2f} referente a quilometragem rodada.'.format(custodias, custokm))
print('Total R${:.2f}'.format(custodias + custokm))
