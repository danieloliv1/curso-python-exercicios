from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(1.5)
print('Seu nome em letras maiúsculas: ',nome.upper())
print('Seu nome em letras minúsculas: ',nome.lower())
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
