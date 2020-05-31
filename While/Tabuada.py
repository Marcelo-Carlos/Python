while True:
    print('-' * 40)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 40)
    if n <= 0:
        print('Programa encerrado. Volte Sempre!')
        break
    else:
        tab = 0
        while tab <= 9:
            tab = tab + 1
            res = n * tab
            print(f'{n} x {tab} = {res}')