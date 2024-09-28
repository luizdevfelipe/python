nu = int(input('Digite um número: '))
f = 1
print('\033[32mO resultado do número {} é'.format(nu))
for c in range(nu, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f, end='')
