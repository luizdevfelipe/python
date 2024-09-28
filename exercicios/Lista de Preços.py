lista = ('Mouse', 100, 'Mousepad', 60, 'Teclado', 300, 'Notebook', 5000, 'Monitor', 800, 'Mesa', 90)
soma = 0
print('-'*40)
print(f'{"PREÇO DO SETUP":^40}')
print('-'*40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}R$', end='')
    else:
        print(f'{lista[pos]:>8.2f}')
        soma += lista[pos]
print('-'*40)
print(f'{"TOTAL":.<30}R${soma:>8.2f}')
