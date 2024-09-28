jogador = dict()  # info jogador
time = []  # todo time
pontos = []  # gols jogador
while True:
    pontos.clear()
    print('=' * 35)
    jogador['Jogador'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["Jogador"]} jogou? '))
    for p in range(0, partidas):
        pontos.append((int(input(f'  Quantos gols na partida {p + 1}? '))))
    jogador['Gols'] = pontos.copy()
    jogador['Total'] = sum(pontos)
    time.append(jogador.copy())
    while True:
        quer = str(input('Quer continuar? [S/N]')).upper()[0]
        if quer in 'SN':
            break
        else:
            print('ERRO! Responta apenas com S/N')
    if quer == 'N':
        break
print('=-' * 30)
for i in jogador.keys():
    print(f'  {i:<15}', end='')
print()
print('=-' * 30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 Stop] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'  Levantamendo do jogador {time[busca]["Jogador"]}')
        for k, v in enumerate(time[busca]['Gols']):
            print(f'    No jogo {k+1} ele fez {v} gols.')
    print('=-' * 30)
print()
print('++++ PROGRAMA ENCERRADO ++++')
