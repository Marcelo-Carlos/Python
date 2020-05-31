from datetime import date
menor = 0
maior = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = date.today().year - nasc
    if idade < 21:
        menor = menor + 1
    else:
        maior = maior + 1
print('{} Pessoas ainda não atingiram a maior idade. {} Pessoas ja atingiram a maior idade'.format(menor, maior))