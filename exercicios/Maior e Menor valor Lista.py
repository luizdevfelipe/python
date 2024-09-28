numeros = list()
menor = maior = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print('-='*30)
print(f'Você digitou os números: {numeros}')
print(f'O MAIOR valor digitado foi {maior} na(s) posição(ões) ', end='')
for pos, v in enumerate(numeros):
    if v == maior:
        print(f'{pos}...', end='')
print(f'\nO MENOR valor digitado foi {menor} na(s) posição(ões) ', end='')
for pos, v in enumerate(numeros):
    if v == menor:
        print(f'{pos}...', end='')
print()
