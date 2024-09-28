nu = int(input('Digite um número: '))
f = 1
print(f'\033[32mO resultado do número {nu}')
while nu > 0:
    print(nu, end='')
    print(' x 'if nu > 1 else ' = ', end='')
    f *= nu
    nu -= 1
print(f, end='')
