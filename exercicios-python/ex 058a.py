from random import randint
from time import sleep
pc = randint(0, 10)
jogador = int(input('De 0 a 10, qual número estou pensando? '))
tentativas = 1
while jogador != pc:
    pc = randint(0, 10)
    print('Poxa, você errou pensei no número {}. Tente novamente!'.format(pc))
    sleep(1)
    jogador = int(input('De 0 a 10, qual número estou pensando? '))
    tentativas += 1
if tentativas == 1:
    print('DE PRIMEIRA!!! Parabéns, pensei no número {} você acertou.'.format(pc))
elif tentativas < 10:
    print('Parabéeeens! Pensei no número {}. Você acertou na {}ª tentativa.'.format(pc, tentativas))
else:
    print('''FINALMENTE! Pensei no número {}. Você acertou na {}ª tentativa.'''.format(pc, tentativas))
