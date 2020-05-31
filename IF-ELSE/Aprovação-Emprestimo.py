from math import trunc

casa = float(input('Qual valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = float(input('Em quantos anos queres financiar? '))

calc = (anos - trunc(anos)) * 10
meses = trunc(anos) * 12 + calc
meses = trunc(meses)

prestacao = casa / meses
renda = (30 / 100 * salario)

if renda >= prestacao:
    print('Seu financiamento foi aprovado com sucesso!')
    print('O valor de sua prestação será R$: {:.2f}'.format(prestacao))
else:
    print('Seu financiamento não foi aprovado. A prestação supera 30% de sua renda que é de no resta R$: {}'.format(renda))
    print('Valor resta da parcela para aprovação é de R$: {:.2f}'.format(restação))