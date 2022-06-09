print('-=-' * 12)
print('Analisador de Triângulos')
print('-=-' * 12)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 < n2 +  n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')
