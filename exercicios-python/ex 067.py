usuario = 0
continuar = 'S'
while continuar not in 'Nn':
    usuario = int(input('Digite um número para ver sua tabuada: '))
    for c in range(1,11):
        print(f'{usuario} x {c} = {usuario*c}')
    continuar = str(input('Quer ver outra tabuada (S/N)? ')).strip().upper()[0]
