vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7.0
if vel <= 80:
    print('Parabens você é prudente!')
else:
    print('Você foi multado em R$: {}'.format(multa))