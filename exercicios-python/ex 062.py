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
sleep(1)
usuario = int(input('\nDeseja ver mais quantos termos? '))
nc = 1
ntermo = termo
while usuario != 0:
    nc = 1
    while nc <= usuario:
        print(ntermo, end='')
        print(' > ' if nc < usuario else '', end='')
        ntermo += razão
        nc += 1
    sleep(1)
    usuario = int(input('\nDeseja ver mais quantos termos? '))
print('OK! Até a próxima.')
