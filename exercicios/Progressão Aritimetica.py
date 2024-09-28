termo = int(input('Primeiro termo: '))
razao = int(input('A razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('\033[1;32m', c, '\033[m', end=' -> ')
print('Acabou')
