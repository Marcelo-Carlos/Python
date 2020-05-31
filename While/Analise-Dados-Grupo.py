print('-'*20)
print('CADASTRE UMA PESSOA')
homens = pessoas = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if idade >= 18:
            pessoas += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
    print('-' * 20)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('-' * 20)
    if continuar == 'N':
        break
print('='*10,'FIM DO PROGRAMA','='*10)
print(f'Total de pessoas com mais de 18 anos: {pessoas}')
print(f'AO todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')