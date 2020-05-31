salario = float(input('Qual seu salário atual? '))
reajuste = int(input('Quanto é o percentual de reajuste? '))
salFinal = salario + (salario * reajuste / 100)
print('Salario aumento foi de {} %, seu salario final é {:.2f}'.format(reajuste, salFinal))

