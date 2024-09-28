analisar = str(input('Digite a expressão: '))
teste = list()
for par in analisar:
    if par == '(':
        teste.append(1)
    if par == ')':
        teste.pop()
if len(teste) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida.')
