print('--- Calculador de média ---')
print('~' * 30)
num = soma = cont = maior = menor = 0
mais = 's'
while mais not in 'Nn':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    mais = str(input('Adicionar mais valores (S/N)? ')).strip()
    while mais.upper() not in 'SN':
        print('Resposta inválida!')
        mais = str(input('Adicionar mais valores (S/N)? ')).strip()
média = soma / cont
print(f'Você digitou {cont} números somando o total de {soma} e a média entre eles é de {média}.')
print(f'O maior número entre eles foi {maior} e o menor número foi {menor}.')
