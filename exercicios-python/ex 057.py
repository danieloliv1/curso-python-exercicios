sexo = str(input('Informe seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dados inválidos!')
    sexo = str(input('Por favor, informe seu sexo (M/F): ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo.upper()))
