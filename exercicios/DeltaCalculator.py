from math import sqrt


def numero(msg):
    while True:
        try:
            nu = int(input(msg))
        except ValueError:
            print('Digite um número válido!')
        else:
            return nu


print('\033[1;31m<<<<< Calculadora de Delta >>>>>\033[m')
a = numero('\033[1;33mValor de A = ')
b = numero('Valor de B = ')
c = numero('Valor de C = \033[m')

Delta = b ** 2 - 4 * a * c
try:
    raiz = sqrt(Delta)
    print(f'\033[34mDelta = {Delta}\033[m')
    print(f'\033[34mRaiz do Delta = {raiz}\033[m')
    print('\033[4;32mx\' = {}'.format((-b + raiz) / (2 * a)))
    print('x\" = {} \033[m'.format((-b - raiz) / (2 * a)))
    print('\n\033[7m====== by lipe00743 ======\033[m')
except:
    print('\033[4;31mNão foi possível calcular o resultado do delta.\033[m')
# a4 b-33 c8
# a1 b1 c1
