valores = list()
for v in range(0, 5):
    nu = (int(input('Digite um valor: ')))
    if v == 0 or nu > valores[-1]:
        print('\033[1mValor adicionado ao final da lista...\033[1m')
        valores.append(nu)
    else:
        pos = 0
        while pos < len(valores):
            if nu <= valores[pos]:
                valores.insert(pos, nu)
                print(f'\033[1mValor adicionado na posição {pos}...\033[m')
                break
            pos += 1
print('='*50)
print(f'Os valores digitados em ordem são {valores}')
