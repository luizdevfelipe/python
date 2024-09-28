numeros = [[], []]
for v in range(1, 8):
    nu = int(input(f'Digite o {v}ª valor: '))
    if nu % 2 == 0:
        numeros[0].append(nu)
    else:
        numeros[1].append(nu)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares foram: {numeros[0]}')
print(f'Os valores ímpares foram: {numeros[1]}')
