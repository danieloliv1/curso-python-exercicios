velocidade = int(input('Digite a velocidade do veículo: '))
multa = (velocidade - 80) * 7
if 88 >= velocidade > 80: #Tolerância de 10%
    print('ATENÇÃO! A velocidade máxima da via é de 80 km/h')
if velocidade > 88:
    print('Veículo acima da velocidade permitida. Penalidade: Multa de R${:.2f}.'.format(multa))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança.')
