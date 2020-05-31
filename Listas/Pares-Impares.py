lista = [[], []] #PRIMEIRO PARTE LISTA NA PARTE 0, SEGUNDO LISTA NA PARTE 1
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=-='*30)
print(f'Todos os valores: {lista}')
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')