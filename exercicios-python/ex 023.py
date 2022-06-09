'''num = int(input('Digite um número de 0 a 9999: '))
n = str(num)
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(n[3], n[2], n[1], n[0]))'''
#Forma de cima tem uma opção de fazer, mas ainda não foi aprendida

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))
