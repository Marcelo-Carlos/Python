print('{:=^40}'.format('LOJAS GUANABARA '))
produto = float(input('Qual valor do produto? '))
print('[ 1 ] À VISTA DINHEIRO OU CHEQUE: 10% DE DESCONTO')
print('[ 2 ] À VISTA CARTÃO: 5% DE DESCONTO')
print('[ 3 ] ATÉ 2x NO CARTÃO: PREÇO NORMAL')
print('[ 4 ] 3x OU MAIS NO CARTÃO: 20% DE JUROS')
pagamento = int(input('Qual das condições acima de pagamento você prefere? '))

if pagamento == 1:
    total = (produto * 10 / 100) - produto
    print('O valor final do produto com 10% de desconto foi de R$: {}'.format(total))
elif pagamento == 2:
    total = (produto * 5 / 100) - produto
    print('O valor final do produto com 5% de desconto foi de R$: {}'.format(total))
if pagamento == 3:
    total = produto
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$: {}'.format(parcela))
elif pagamento == 4:
    total = (produto * 20 / 100) + produto
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R$:{:.2f} COM JUROS'.format(totparc, parcela))
    print('O valor final do produto com 20% de juros foi de R$: {}'.format(total))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!')