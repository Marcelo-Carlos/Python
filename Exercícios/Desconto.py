preco = float(input('Qual preço do produto: '))
desc = float(input('Qual desconto: '))
precoFinal = preco - (preco * desc / 100)
print('O valor com desconto é de R$: {:.2f}'.format(precoFinal))