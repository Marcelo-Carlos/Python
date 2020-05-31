from math import factorial
num = int(input('Digite um número para obter o fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))

#FORMA TRADICIONAL ABAIXO

num = int(input('Digite um número para obter o fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while num > 0:
    print('{}'.format(num), end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
    num = num - 1
print('{}'.format(f))

