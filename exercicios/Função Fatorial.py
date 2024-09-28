def fatorial(nu, show=False):
    """
    =-= Calcula o resultado de um número =-=
    :param nu: O número a ser calculado
    :param show: Mostra ou não a multiplicação
    :return: exibe o resultado
    """
    print('=-'*15)
    fat = 1
    for c in range(nu, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(fatorial(5, show=True))
