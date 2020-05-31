nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('REPROVADO! Sua média foi {}. Minimo seria 7,0'.format(media))
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO! Sua média foi {}'.format(media))
else:
    print('APROVADO! Sua média foi {}'.format(media))