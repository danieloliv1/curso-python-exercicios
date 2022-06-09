n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O \033[1mPRIMEIRO\033[m número é \033[1mmaior\033[m.')
elif n2 > n1:
    print('O \033[1mSEGUNDO\033[m número é \033[1mmaior\033[m.')
elif n1 == n2:
    print('Não existe maior. Os dois são iguais.')
