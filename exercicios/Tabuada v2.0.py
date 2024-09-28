print('\033[1;31m=-='*3, 'Tabuada v2.0', '=-='*3)
nu = int(input('\033[mDigite um número para ver sua tabuada: '))
print('\033[1;32m=-='*5)
for c in range(1, 11):
    print('{} X {:2} =  {}'.format(nu, c, c * nu))
print('=-='*5)
