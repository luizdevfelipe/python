soma = 0
cont = 0
for c in range(1, 7):
    nu = int(input('Digite o {}º valor '.format(c)))
    if nu % 2 == 0:
        soma += nu
        cont += 1
print('Você informou {} número(s) par(es) e a soma foi {}'.format(cont, soma))
