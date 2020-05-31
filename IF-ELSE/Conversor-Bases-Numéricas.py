num = int(input('Digite um numero inteiro: '))
print(' [ 1 ] Binário')
print(' [ 2 ] Octal')
print(' [ 3 ] Hexadecimal')
conv = int(input('Em que deseja converter? '))

if conv == 1:
    print('A conversão é: {}'.format(bin(num)[2:]))
elif conv == 2:
    print('A conversão é: {}'.format(oct(num)[2:]))
elif conv == 3:
    print('A conversão é: {}'.format(hex(num)[2:]))
else:
    print('Opção inválida. Digite 1, 2 ou 3')