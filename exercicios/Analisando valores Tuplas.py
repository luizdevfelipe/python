nu = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'O número 9 apareceu {nu.count(9)} vez(es).')
if 3 in nu:
    print(f'O número 3 apareceu na {nu.index(3)+1}ª posição.')
else:
    print('Não teve nenhum número 3.')
print('Os números pares foram: ', end='')
for c in nu:
    if c % 2 == 0:
        print(f'{c}', end=' ')
