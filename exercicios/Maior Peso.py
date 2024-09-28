maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('O peso da {}ª pessoa é '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}Kg e o menor de {}Kg'.format(maior, menor))
