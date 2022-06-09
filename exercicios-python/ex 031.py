dist = float(input('A quantos quilômetros está o seu destino? '))
'''if dist <=200:
    print('O valor da passagem ficará R${:.2f}.'.format(dist * 0.50))
else:
    print('O valor da passagem ficará R${:.2f}.'.format(dist * 0.45))'''
preço = dist * 0.50  if dist <= 200 else dist * 0.45
print('O valor da passagem ficará R${:.2f}.'.format(preço))
