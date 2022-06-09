from time import sleep
inicio = int(input('Início da PA: '))
razão = int(input('Razão da PA: '))
termo = inicio
c = 1
while c <= 10:
    print(termo, end='')
    print(' > ' if c < 10 else '', end='')
    termo += razão
    c += 1
