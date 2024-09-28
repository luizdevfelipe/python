from time import sleep
c = ('\033[m',    # 0 - sem cor
     '\033[1;41m',  # 1 - vermelho
     '\033[1;42m',  # 2 - verde
     '\033[1;43m',  # 3 - amarelo
     '\033[1;44m',  # 4 - azul
     '\033[1;7m'    # 5 - branco
     )


def titulo(msg, cor=0):
    """
    !! Coloca [~~~] adaptáveis ao tamnho da frase. !!
    :param msg: Mensagem a ser exibida.
    :param cor: (opcional) Se utilizar uma tupla com o código de cores
    é possivel selecionar a cor seguindo a ordem dela na tupla.
    :return: Mostra a frase com [~~~] em cima e em baixo dela.
    """
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    """
    !! Mostra o manual de uma função ou biblioteca. !!
    :param com: Recebe o nome da biblioteca.
    :return: Exibe seu manual com cores, requer um tupla.
    com os códigos das cores que desejar em suas devidas posições.
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    print(help(com))
    print(c[0], end='')
    sleep(2)


while True:
    titulo('Sistema de Ajuda PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        titulo('PROGRAMA ENCERRADO', 1)
        break
    else:
        ajuda(comando)
