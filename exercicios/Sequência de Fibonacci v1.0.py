termos = int(input('Quantos termos deja ver? '))
t1 = 0
t2 = 1
cont = 3
print('A sequencia de Fibonacci com {} termo(s) é essa:'.format(termos))
print('\033[1;32m{} \033[m-> \033[1;32m{}\033[m'.format(t1, t2), end=' -> ')
while cont <= termos:
    t3 = t1 + t2
    print('\033[1;32m{}\033[m'.format(t3), end=' -> ')
    cont += 1
    t1 = t2
    t2 = t3
print('Acabou')
5