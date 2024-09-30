from random import sample
from time import sleep


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, SyntaxError):
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar um valor.')
            return 0
        else:
            return n


def valores():
    while True:
        escolha = leiaint('Sua escolha: ')
        if escolha == 1:
            facil = sample(range(0, 10), 3)
            return facil
        elif escolha == 2:
            medio = sample(range(0, 30), 3)
            return medio
        elif escolha == 3:
            dificil = sample(range(0, 50), 3)
            return dificil
        else:
            print('Opção não encontrada! Escolha de 1 a 3.')
            
#-----------------------------------------------------------------------------

print('=-='*13)
print('Eu pensei em 3 números, tente adivinhar.')
print('''        Eles podem estar entre:

1 - Fácil 0 a 10
2 - Médio 0 a 30
3 - Difícil 0 a 50
''')
print('=-='*13)

confirmar = valores()


total = 0
while True:
    print('=-=' * 13)
    jogada = leiaint('Digite o número que pensei: ')
    total += 1
    if jogada in confirmar:
        confirmar.remove(jogada)
        print('Acertou um valor!')
    elif jogada == 999:
        print(confirmar)
    for v in confirmar:
        if jogada > v:
            print(f'Temos um valor MENOR que {jogada}')
        else:
            print(f'Temos um valor MAIOR que {jogada}')
    if len(confirmar) == 0:
        print(f'\nVocê acertou TODOS! Com {total} tentativas.')
        sleep(15)
        break
