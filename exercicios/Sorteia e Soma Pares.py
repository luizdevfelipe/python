from time import sleep
from random import randint
numeros = []


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('=-'*30)
    print(f'Sorteando 5 valores da lista: ', end='')
    for nu in numeros:
        print(nu, end=' ')
        sleep(0.5)
    print('PRONTO!')
    print('=-'*30)


def somaPar():
    soma = 0
    for v in numeros:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores Pares de {numeros}, temos o resultado {soma}')


sorteia()
somaPar()
