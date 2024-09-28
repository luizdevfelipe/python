frase = str(input('Digite a frase: ')).strip().upper().split()
juntar = ''.join(frase)
inverso = ''
for letra in range(len(juntar) - 1, -1, -1):
    inverso += juntar[letra]
print('O inverso de {} é {}.'.format(juntar, inverso))
if inverso == juntar:
    print('Temos um Palíndromo.')
else:
    print('Não é um Palíndromo.')
