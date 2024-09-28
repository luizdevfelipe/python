from random import randint
from time import sleep
computador = randint(1, 3)
print('\033[1;32m=-='*7)
print('''PEDRA PAPEL TESOURA
Escolha sua jogada:
1 - Pedra
2 - Papel
3 - Tesoura''')
print('=-='*7)
opcao = int(input('\033[mSua Jogada: '))
while not 0 < opcao < 4:
    print('\033[31mOpção inválida\033[m')
    opcao = int(input('Sua Jogada: '))
print('\033[1;34mPedra')
sleep(1)
print('Papel')
sleep(1)
print('TESOURA!!!\033[m')
sleep(1)
if opcao == 1 and computador == 2:
    print('O computador ganhou ele jogou Papel e você Pedra.')
elif opcao == 1 and computador == 3:
    print('Você ganhou o computador jogou Tesoura e você Pedra.')
elif opcao == 2 and computador == 1:
    print('Você ganhou o computador jogou Pedra e você Papel.')
elif opcao == 2 and computador == 3:
    print('O computador ganhou ele jogou Tesoura e você Papel.')
elif opcao == 3 and computador == 1:
    print('O computador ganhou ele jogou Pedra e você Tesoura.')
elif opcao == 3 and computador == 2:
    print('Você ganhou o computador jogou Papel e você Tesoura.')
else:
    if computador == 1:
        computador = 'Pedra'
    elif computador == 2:
        computador = 'Papel'
    else:
        computador = 'Tesoura'
    print('\033[33mDeu Empate vocês jogaram {}.'.format(computador))
