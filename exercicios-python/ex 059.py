from time import sleep
n1 = float(input('1º valor: '))
n2 = float(input('2º valor: '))
usuario = 1
maior = n1
if n1 < n2:
    maior = n2
while usuario != 5:
    soma = n1 + n2
    mult = n1 * n2
    print('''Menu:
    ( 1 ) somar
    ( 2 ) multiplicar
    ( 3 ) maior
    ( 4 ) novos números
    ( 5 ) sair do programa''')
    usuario = int(input('\033[34mDigite sua opção:\033[m '))
    if usuario == 1:
        print('O resultado da soma é {:.2f}.'.format(soma))
    elif usuario == 2:
        print('O resultado da multiplicação é {:.2f}.'.format(mult))
    elif usuario == 3:
        if n1 > n2:
            maior = n1
            print('O maior valor é {}.'.format(maior))
        elif n2 > n1:
            print('O maior valor é {}.'.format(maior))
        else:
            print('Os dois valores são {}. São iguais.'.format(n1))
    elif usuario == 4:
        n1 = float(input('1º valor: '))
        n2 = float(input('2º valor: '))
    elif usuario < 1 or usuario > 5:
        print('\033[31mOpção inválida!\033[m')
    sleep(1)
print('Até a próxima!')
