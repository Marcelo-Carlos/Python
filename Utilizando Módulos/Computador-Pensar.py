from random import randint

computador = randint(0, 5) #sorteia um numero#
print('-=-'* 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? '))#jogador tenta adivinhar#
if jogador == computador:
    print('Parabens você acertou!')
else:
    print('Você errou!')