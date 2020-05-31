from random import randint
from time import sleep
from operator import itemgetter #PARA ORDENAR PELO VALOR NA POSIÇÃO 1
jogo = {'jogador1': randint(0, 6),
        'jogador2': randint(0, 6),
        'jogador3': randint(0, 6),
        'jogador4': randint(0, 6)}
ranking = [] # PARA COLOCAR EM ORDEM FOI CRIADO UMA LISTA DEVIDO O RESULTADO ESTÁ EM FORMA DE LISTA
print('VALORES SORTEADOS: ')
for k, v in jogo.items(): #UTILIZA-SE A CHAVE E O VALOR
    print(f'{k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#SE FOR 0 COLOCA POR ORDEM DE CHAVE, 1 EM ORDEM DE VALOR
print('=-='*20)
print('Ranking dos Jogadores: ')
for i, v in enumerate(ranking):#REVERSE ACIMA FOI UTILIZADO PARA COLOCAR EM FORMA DECRESCENTE
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)#FOI UTILIZADO ACIMA O ENUMERATE DEVIDO SE TRATAR DE LISTA. SE FOSSE DIC SERIA ITEMS

jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]#PARA COLOCAR A LISTA DENTRO DO DICIONÁRIO
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')