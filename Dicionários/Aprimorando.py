jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]#PARA COLOCAR A LISTA DENTRO DO DICIONÁRIO
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())#PARA FAZER A CÓPIA DE UM DICIONÁRIO USA-SE O COPY, NA LISTA USA-SE [:]
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*40)#ACIMA SÃO LIDOS TODOS OS DADOS DOS JOGADORES
print('cod ', end='')#ABAIXO SÃO MOSTRADOS TODOS OS DADOS - ANALISE DOS DADOS
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código da {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
