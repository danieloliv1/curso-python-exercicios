nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print('Primeiro nome: {}'.format(separado[0]))
print('Último nome: {}'.format(separado[len(separado)-1]))
