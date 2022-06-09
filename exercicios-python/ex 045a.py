from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Suas opções:
0 para PEDRA
1 para PAPEL
2 para TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('Você {} x {} Computador'.format(itens[jogador], itens[pc]))
if pc == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU')
    else:
        print('OPÇÃO INVÁLIDA!')
elif pc == 1:
    if jogador == 0:
        print('VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA!')
elif pc ==2:
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('OPÇÃO INVÁLIDA!')
