import random
from time import sleep
print('''Suas opções:
( 0 ) PEDRA
( 1 ) PAPEL
( 2 ) TESOURA''')
jogador = int(input('Qual é sua jogada? '))
if jogador == 0:
    jogador = 'PEDRA'
elif jogador == 1:
    jogador = 'PAPEL'
elif jogador == 2:
    jogador = 'TESOURA'
opções = ['PEDRA', 'PAPEL', 'TESOURA']
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POH!!!')
pc = random.choice(opções)
if jogador == 'PEDRA' and pc == 'TESOURA':
    print('Você {} x {} Computador'.format(jogador, pc))
    print('Você Ganhou!')
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print('Você {} x {} Computador'.format(jogador, pc))
    print('Você Ganhou!')
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print('Você {} x {} Computador'.format(jogador, pc))
    print('Você Ganhou!')
elif jogador == pc:
    print('Você {} x {} Computador'.format(jogador, pc))
    print('EMPATE. TENTE NOVAMENTE!')
else:
    print('Você {} x {} Computador'.format(jogador, pc))
    print('Você Perdeu! Tente novamente.')
