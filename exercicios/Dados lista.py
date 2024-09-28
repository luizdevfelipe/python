lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    quer = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if quer == 'N':
        break
print('-='*20)
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O número 5 está na lista')
else:
    print('Não encontrei o número 5 na lista.')
