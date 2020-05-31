sal = float(input('Digite seu salário: '))
if sal <= 1250:
    aumento = sal + (sal * 10 / 100)
    print('Seu novo salario é R$: {}'.format(aumento))
else:
    aumento = sal + (sal * 15 / 100)
    print('Seu novo salário é: {}'.format(aumento))