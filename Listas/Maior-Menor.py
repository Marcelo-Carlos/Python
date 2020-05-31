numeros = []
maior = menor = c = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0 or maior < numeros[c]:
        maior = numeros[c]

    if c == 0 or menor > numeros[c]:
        menor = numeros[c]

print('=-='*20)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor foi {maior} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor foi {menor} na posições ', end=' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}... ', end='')
print()
