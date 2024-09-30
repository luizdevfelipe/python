from os import startfile, chdir, listdir, makedirs, path

lista = []
local = []
documents = path.expanduser('~/Documents/GamesExec')


def linha():
    print('-=-' * 13)


def leia_int(msg):
    while True:
        try:
            nu = int(input(msg))
        except ValueError or SyntaxError:
            print('ERRO! Digite um número inteiro válido.')
        else:
            return nu


def mostrar_jogos():
    cont = 0
    with open('games.txt', 'r') as arq:
        for valor in arq:
            print(f'{cont} - {valor}', end='')
            cont += 1


def perguntar_direct(msg):
    folder = str(input(msg)).strip()
    with open('pasta.txt', 'w') as diretorio:  # salva o diretório
        diretorio.write(folder)


def salvar_dados():
    with open('pasta.txt', 'r') as diretorio:
        folder = diretorio.readline()
    try:
        listdir(folder)
    except FileNotFoundError:
        print('ERRO! Não foi possível encontrar nenhum jogo na pasta informada.')
        perguntar_direct('Digite o diretório da pasta novamente para corrigir: ')
        salvar_dados()
    finally:
        with open('pasta.txt', 'r') as diretorio:
            folder = diretorio.readline()
        atalhos = listdir(folder)

    if 'desktop.ini' in atalhos:
        atalhos.remove('desktop.ini')
    with open('games.txt', 'w') as arq:
        for itens in atalhos:
            arq.write(f'{itens}\n')


def cabecalho():
    print('O que deseja abrir/fazer?')
    print('''0 - *Mudar Pasta*

    1 - Discord
    2 - Música
    3 - Somente o Jogo''')


try:
    chdir(documents)
except FileNotFoundError:
    makedirs(documents)
finally:
    chdir(documents)
    abrir_games = open('games.txt', 'a')
    abrir_games.close()
    abrir_pasta = open('pasta.txt', 'a')
    abrir_pasta.close()


# Código Principal =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=

with open('pasta.txt', 'r') as file:
    ler = file.readline()
if ler == '':
    print('*Crie uma pasta e coloque todos os atalhos de seus jogos nela*')
    perguntar_direct('Digite o diretório dessa pasta: ')
    salvar_dados()
else:
    salvar_dados()

linha()
cabecalho()
jogadores = leia_int('Opção: ')

while not jogadores > 0:
    if jogadores == 0:
        linha()
        perguntar_direct('Digite o novo diretório: ')
        salvar_dados()
        linha()
        cabecalho()
        jogadores = leia_int('Opção: ')

linha()
print('O que deseja jogar?\n')
mostrar_jogos()
linha()

with open('pasta.txt', 'r') as file:  # salva o diretório na lista do startfile
    local.append(file.readline())

with open('games.txt', 'r') as arquivo:  # lê o arquivo e tira o \n para executar
    for i in arquivo:
        lista.append(f'{i}'.replace('\n', ''))
jogo = leia_int('Número: ')

startfile(rf'{local[0]}\{lista[jogo]}')

# A Fazer: descobrir os diretórios padrões destes dois aquivos
if jogadores == 1:
    startfile(r'C:\Users\user\Discord.lnk')
elif jogadores == 2:
    startfile(r'C:\Microsoft.Media.Player.lnk')
