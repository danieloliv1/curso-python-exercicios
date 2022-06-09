from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    print('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(ano + 18))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos atrás em {}.'.format(idade - 18, ano + 18))
