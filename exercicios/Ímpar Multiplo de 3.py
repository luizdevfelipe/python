soma = 0
cont = 0
for c in range(1, 501):  # o dele ele coloca  ,2 e o resultado fica 20667 e 83
    if c % 3 == 0:
        cont = cont + 1  # cont += 1
        soma = soma + c  # soma += c
print('A soma de todos os {} valores é {}'.format(cont, soma))
