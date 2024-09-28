from random import randint
nu = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),
      randint(1, 10))
print('Os números sorteados foram:', end=' ')
for c in nu:
      print(f'{c}', end=' ')
print(f'\nO maior número foi {max(nu)}')
print(f'O menor número foi {min(nu)}')
