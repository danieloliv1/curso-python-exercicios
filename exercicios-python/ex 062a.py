from time import sleep
inicio = int(input('Início da PA: '))
razão = int(input('Razão da PA: '))
termo = inicio
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} > '.format(termo), end='')
        termo += razão
        c += 1
    print('Pronto!')
    sleep(0.5)
    mais = int(input('\nDeseja ver mais quantos termos? '))
print('OK! {} termos foram mostrados. Até mais!'.format(total))
