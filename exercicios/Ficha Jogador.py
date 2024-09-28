def ficha(nome='<desconhecido>', gols=0):
    print('=-'*15)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip().title()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
