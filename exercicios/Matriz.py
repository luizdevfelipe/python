lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c] % 2 == 0:
            somap += lista[l][c]
    print()
print('='*30)
print(f'A soma dos números pares é {somap}')
for l in range(0, 3):
    somac += lista[l][2]
print(f'A soma da terceira coluna é {somac}')
for c in range(0, 3):
    if c == 0:
        maior = lista[1][c]
    elif lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior elemento da 2ª linha é {maior}')
