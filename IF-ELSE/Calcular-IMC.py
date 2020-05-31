altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('ABAIXO DO PESO! Seu IMC foi de: {:.1f}'.format(imc))
elif 18.5 <= imc <= 25:
    print('PESO IDEAL! Seu IMC foi de: {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('SOBREPESO! Seu IMC foi de: {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Obesidade! Seu IMC foi de: {:.1f}'.format(imc))
else:
    print('OBESIDADE MORBIDA! Seu IMC foi de: {:.1f}'.format(imc))