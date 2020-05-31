dist = float(input('Qual a distancia de sua viagem? '))
if dist <= 200:
    preco = dist * 0.50
    print('O custo de sua viagem será de R$: {:.2f}'.format(preco))
else:
    preco = dist * 0.45
    print('O custo de sua viagem será de R$: {:.2f}'.format(preco))