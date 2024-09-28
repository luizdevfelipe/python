from random import randint
facil = randint(0, 10)
medio = randint(0, 30)
dificil = randint(0, 50)
total = ordem = 0
acertou = False
print('\033[33m=-='*13)
print('Eu pensei em um número, tente adivinhar.')
print('''Ele pode estar entre:

1 - Fácil 0 a 10
2 - Médio 0 a 30
3 - Difícil 0 a 50
''')
print('=-='*13)
escolha = int(input('\033[mSua escolha: '))
while not 0 < escolha < 4:
    print('\033[31mNão encontrei essa opção.\033[m')
    escolha = int(input('\033[mSua escolha: '))
if escolha == 1:
    ordem = facil
elif escolha == 2:
    ordem = medio
elif escolha == 3:
    ordem = dificil
while not acertou:
    jogada = int(input('Digite o número que pensei: '))
    total += 1
    if jogada == ordem:
        acertou = True
    else:
        if jogada > ordem:
            print('\033[34mMenos... Tente de novo.\033[m')
        else:
            print('\033[34mMais... Tente de novo.\033[m')
print('\033[1;32mVocê acertou! Com {} tentativas.'.format(total))
