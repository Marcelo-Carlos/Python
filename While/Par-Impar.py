from random import randint
print('-=-'*10)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-'*10)
tot = 0
vit = 0
while True:
    computador = randint(0, 11)
    jogador = int(input('Diga um valor: '))
    tot = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total {tot}')
    print('DEU PAR!' if tot % 2 == 0 else 'DEU IMPAR!')
    if tipo == 'P':
        if tot % 2 == 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU')
            break
    if tipo == 'I':
        if tot % 2 == 1:
            print('Você VENCEU!')
            vit += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-' * 40)
print(f'GAME OVER! Você venceu {vit} vezes')