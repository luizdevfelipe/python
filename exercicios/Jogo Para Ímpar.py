from random import randint
vitoria = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um número: '))
    jogada = ' '
    soma = jogador + computador
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}')
    print('Deu Par'if soma % 2 == 0 else 'Deu Ímpar')
    if jogada == 'P':
        if soma % 2 == 0:
            print('\033[32mVocê Ganhou.\033[m')
            vitoria += 1
        else:
            print('\033[31mO Computador Ganhou.\033[m')
            break
    elif jogada == 'I':
        if soma % 2 == 1:
            print('\033[32mVocê Ganhou.\033[m')
            vitoria += 1
        else:
            print('\033[31mO Computador Ganhou.\033[m')
            break
    print('Jogue Novamente.')
print(f'\033[33mGame Over. Você venceu {vitoria} vezes.\033[m')
