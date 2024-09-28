valores = list()
while True:
    nu = (int(input('Digite um número: ')))
    if nu not in valores:
        valores.append(nu)
        print('\033[1mValor Adicionado!\033[m')
    else:
        print('\033[1mValor Removido! Já está na lista!\033[m')
    parada = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if parada == 'N':
        break
valores.sort()
print('='*50)
print(f'Você digitou os valores {valores}')
