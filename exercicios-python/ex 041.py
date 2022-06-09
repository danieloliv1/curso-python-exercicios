from datetime import date
print('\033[1;34m-=- Confederação Nacional de Natação -=-\033[m')
nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('O atleta tem \033[1;31m{}\033[m anos.'.format(idade))
categoria = 'MIRIM'
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
elif idade > 25:
    categoria = 'MASTER'
print('Classificação: categoria \033[1;31m{}\033[m.'.format(categoria))
