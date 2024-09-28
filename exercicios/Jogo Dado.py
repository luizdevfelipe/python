from random import randint
from operator import itemgetter
from time import sleep
jogadores = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)
             }
print('JOGANDO DADO...')
for k, v in jogadores.items():
    print(f'O {k} tirou o número {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=-'*16)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)
