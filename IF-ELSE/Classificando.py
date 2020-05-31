from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
if idade <= 19:
    print('JUNIOR')
elif idade < 20:
    print('SENIOR')
else:    
    print('MASTER')


    