from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print('---------------- MENU ------------------')
    print('\n [ 1 ] SOMAR \n [ 2 ] MULTIPLICAR \n [ 3 ] MAIOR \n [ 4 ] NOVOS NÚMEROS \n [ 5 ] SAIR DO PROGRAMA \n')
    op = int(input('QUAL OPERAÇÃO DESEJA FAZER? '))
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif op == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Saindo...')
    else:
        print('Opção inválida!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')