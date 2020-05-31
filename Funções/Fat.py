def fatorial(n, show=False):# PARAMETRO OPCIONAL
    """
    -> Calcula o fatotial de um número.
    :param n: O número a ser calculado
    :param show: (opcinal) Mostrar ou não a conta
    :return: Retorna o valor do fatotial de um numero
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#PROGRAMA PRINCIPAL
print(fatorial(5, show=True))
print(fatorial(int(input('Digite um número: ')), show=True))