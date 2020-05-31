num = int(input('Digite um número inteiro de 0 a 10: '))
for c in range(0, 11):
    s = num * c
    print(num, 'x', c, '=', s)

#OUTRA FORMA SIMPLIFICADA

num = int(input('Digite um número inteiro de 0 a 10: '))
for c in range(0, 11):
    print('{} X {:2} = {}'.format(num, c, num * c))