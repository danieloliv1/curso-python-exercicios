from random import randint
from time import sleep
pc = randint(0, 10)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('De 0 a 10, qual número estou pensando? '))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else:
        if pc > jogador:
            print('Mais... Tente mais uma vez.')
        elif pc < jogador:
            print('Menos... Tente mais uma vez.')
if tentativas == 1:
    print('DE PRIMEIRA!!! Parabéns, pensei no número {} você acertou.'.format(pc))
elif tentativas < 4:
    print('Parabéeeens! Pensei no número {}. Você acertou na {}ª tentativa.'.format(pc, tentativas))
else:
    print('''FINALMENTE! Pensei no número {}. Você acertou na {}ª tentativa.'''.format(pc, tentativas))
