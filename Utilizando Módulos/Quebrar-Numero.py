import math
n = float(input('Digite um número: '))
print('O valor digitado foi {}. A porção inteira é: {:.0f}'.format(n, math.trunc(n)))

# outra opção de execução 

from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi {}. A porção inteira é: {:.0f}'.format(n, trunc(n)))

# outra opção de execução 

n = float(input('Digite um número: '))
print('O valor digitado foi {}. A porção inteira é: {:.0f}'.format(n, int(n)))
