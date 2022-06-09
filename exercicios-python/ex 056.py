soma_idade = 0
mulher = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1
média = soma_idade / p
print('A média de idade do grupo é de {} anos.'.format(média))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho.upper()))
print('{} mulher(es) tem menos de 20 anos.'.format(mulher))
