n = c = s = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    if n != 999:
        c += 1
        s += n
print('Foram {} números digitados e a soma foi {}'.format(c, s))