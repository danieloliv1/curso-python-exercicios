import random
import time
pc = random.randint(1, 5) # Faz o computador "PENSAR"
print('-=-' *20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
time.sleep(1.5)
if jogador == pc:
    print('Parabéeeens! Você acertou :)')
else:
    print('ERROOOU! Pensei no número {}. Tente novamente!'.format(pc))
