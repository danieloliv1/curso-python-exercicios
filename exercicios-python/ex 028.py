import random
npc = random.randint(1, 5)
n1 = int(input('De 1 a 5, qual número o computador está pensando agora? '))
if n1 == npc:
    print('Parabéns! Você acertou.')
else:
    print('Não foi dessa vez. Tente novamente!')
