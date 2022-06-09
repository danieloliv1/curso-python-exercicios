p1 = float(input('Nota P1: '))
if p1 < 0 or p1 > 10:
    raise ValueError('Valor de nota P1 inválido!')
p2 = float(input('Nota P2: '))
if p2 < 0 or p2 > 10:
    raise ValueError('Valor de nota P1 inválido!')
média = (p1 + p2) / 2
if média <= 5:
    print('Sua média é de {:.1f}. Você foi \033[1;31mREPROVADO!\033[m'.format(média))
elif 5 <= média < 7:
    print('Sua média é de {:.1f}. Você está de \033[1;34mRECUPERAÇÃO!\033[m'.format(média))
elif média >= 7:
    print('Sua média é de {:.1f}. Você foi \033[1;32mAPROVADO!\033[m'.format(média))
