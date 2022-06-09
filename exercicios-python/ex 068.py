from random import randint
jogador = 'vence'
c = 0
while jogador == 'vence':
    jogador = str(input('Par ou Ímpar? ')).strip().upper()[0]
    valor_jogador = int(input('Qual a sua jogada? '))
    pc = randint(1, 2)
    soma = pc + valor_jogador
    if jogador in 'P':
        if soma % 2 ==0:
            print('Você venceu!')
            jogador = 'vence'
            c += 1
        else:
            print('Fim de jogo. Você perdeu!')
    if jogador in 'I':
        if soma % 2 != 0:
            print('Você venceu!')
            jogador = 'vence'
            c += 1
        else:
            print(f'Fim de jogo. Você perdeu! \nO computador escolheu {pc}')
print(f'Mas você conseguiu conquistar {c} vitórias.')
