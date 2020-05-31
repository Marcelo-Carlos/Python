soma = 0
c = 0
for c in range(0, 6):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        c += 1
print('Você informou {} números PARES e a soma foi {}'.format(c, soma))