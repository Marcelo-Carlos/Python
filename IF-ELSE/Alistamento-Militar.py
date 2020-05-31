from datetime import date

nasc = int(input('Qual sua data de nascimento? '))
idade = date.today().year - nasc
if idade < 18:
    print('Ainda não está na hora de se alistar! Falta(m) {} ano(s)'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar!')
else:
    print('Já passou da hora de se alistar! Já ultrapassou {} ano(s)'.format(idade - 18))