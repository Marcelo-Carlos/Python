sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]#PEGA SÓ A PRIMEIRA LETRA
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} cadastrado com sucesso!'.format(sexo))