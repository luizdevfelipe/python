termo = int(input('Primeiro Termo: '))
razao = int(input('A razão: '))
dez = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while dez <= total:
        print('\033[1;32m{}\033[m -> '.format(termo), end='')
        termo += razao
        dez += 1
    print('Pausa', end='')
    mais = int(input('\nQuer mostrar mais quantos termos? 0 para Sair '))
    print('Progressão encerrada foram apresentados {} termos.'.format(total))
