from datetime import date
ano_atual = date.today().year
maior = 0
for c in range(1, 8):
    ano = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    if ano_atual - ano > 20:
        maior += 1
print('{} dessas pessoas atingiram a maioridade.'.format(maior))
