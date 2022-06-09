peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura * altura)
print('O IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está com o peso idel.')
elif imc < 30:
    print('Você está com SOBREPESO. Tome cuidado!')
elif imc < 40:
    print('Você atingiu a OBESIDADE.')
elif imc >= 40:
    print('Você atingiu a OBESIDADE MÓRBIDA.')
