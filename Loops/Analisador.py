media = 0
idadehomem = 0
nomehomem = ''
totmulher = 0
for c in range(1, 3):
    print('----- {}º PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = float(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media = (media + idade) / c

    if c == 1 and sexo in 'M':
        nomehomem = nome
        idadehomem = idade
    if sexo in 'M' and idade > idadehomem:
        idadehomem = idade
        nomehomem = nome
    if sexo in 'F' and idade > 20:
        totmulher += 1




print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(idadehomem, nomehomem))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(totmulher))