casa = float(input('Digite o valor do imóvel desejado: R$'))
salário = float(input('Digite o valor do seu salário mensal: R$'))
tempo = int(input('Em quantos anos deseja quitar seu imóvel? '))
parcela = casa / tempo / 12
print('Para pagar uma casa de R${:.2f} em {} anos, o valor da parcela mensal será de R${:.2f}.'.format(casa, tempo, parcela))
if parcela <= salário * 0.30:
    print('O empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
