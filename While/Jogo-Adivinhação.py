from random import randint
computador = randint(0, 10)
print('-=-'* 10)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Parabéns você acertou com {} palpites!'.format(palpites))