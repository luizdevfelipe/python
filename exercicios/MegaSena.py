from time import sleep
from random import randint
print('='*30)
print(f'{"Mega Sena":^30}')
print('='*30)
qtd = int(input('Quer sortear quantas jogadas? '))
print('-='*3, f' Sorteando {qtd} Jogos ', '-='*3)
lista = []
jogos = []
tot = 1
while tot <= qtd:
    cont = 0
    while True:
        sorteio = randint(1, 60)
        if sorteio not in lista:
            lista.append(sorteio)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    sleep(1)
    print(f' Jogo {i+1}: {l}')
print('\033[32m=== Boa Sorte ===')
