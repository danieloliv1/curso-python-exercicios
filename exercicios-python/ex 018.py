import math
ângulo = float(input('Digite o valor do ângulo: '))
'''rad = ângulo * math.pi/180'''
rad = math.radians(ângulo)
print('O seno desse ângulo é {:.3f}'.format(math.sin(rad)))
print('O cosseno desse ângulo é {:.3f}'.format(math.cos(rad)))
print('A tangente desse ângulo é {:.3f}'.format(math.tan(rad)))
