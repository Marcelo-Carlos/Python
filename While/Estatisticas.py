print('-'*30)
print(' '*5, 'LOJA SUPER BARATÃO')
print('-'*30)
total = totmil = menor = c = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    total += preco
    c += 1
    if preco > 1000:
        totmil += 1
    if c == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? ')).strip().upper()[0]
        print('-' * 20)
    if resp == 'N':
        break
print(f'O total da compra foi R$: {total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$: 1000.00')
print(f'O produto mais barato foi {barato} que custa R$: {menor}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))