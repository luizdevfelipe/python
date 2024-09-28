termo = int(input('Primeiro Termo: '))
razao = int(input('A razão: '))
dez = 1
while dez <= 10:
    print('\033[1;32m{}\033[m -> '.format(termo), end='')
    termo += razao
    dez += 1
print('Acabou')
