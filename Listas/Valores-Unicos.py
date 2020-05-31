lista = []
while True:
    valores = int(input('Digite um valor: '))
    if valores not in lista:
        lista.append(valores)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('=-='*20)
print(f'Você digitou os valores {sorted(lista)}')