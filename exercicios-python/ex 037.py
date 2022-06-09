num = int(input('Digite um número inteiro: '))
base = int(input('''Escolha uma das bases para conversão.
\033[1;34m1\033[m para \033[1;31mbinário\033[m
\033[1;34m2\033[m para \033[1;31moctal\033[m
\033[1;34m3\033[m para \033[1;31mhexadecimal\033[m
\033[1;4;34mDigite aqui sua opção:\033[m '''))
binário = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]
if base == 1:
    print('\033[4m{}\033[m convertido para BINÁRIO é igual a {}'.format(num, binário))
elif base == 2:
    print('\033[4m{}\033[m convertido para OCTAL é igual a {}.'.format(num, octal))
elif base == 3:
    print("\033[4m{}\033[m convertido para HEXADECIMAL é igual a {}.".format(num, hexadecimal))
else:
    print('Opção inválida. Tente novamente!')
