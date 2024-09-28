nu = int(input('Digite um número: '))
total = 0
for c in range(1, nu + 1):
    if nu % c == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(nu, total))
if total == 2:
    print('Por isso o número \033[7mÉ primo.\033[m')
else:
    print('Por isso o número \033[7mNão é primo.\033[m')
