from math import hypot
catOp = float(input('Digite o cateto oposto: '))
catAd = float(input('Digite o cateto adjacente: '))
hipotenusa = math.hypot(catOp, catAd)
print('A hipotenusa é {:.2f}'.format(hipotenusa))

# Outra opção de execução sem uso de biblioteca

catOp = float(input('Digite o cateto oposto: '))
catAd = float(input('Digite o cateto adjacente: '))
hipot = (catOp ** 2 + catAd ** 2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hipot))






