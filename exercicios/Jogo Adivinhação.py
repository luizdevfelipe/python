from random import randint
from time import sleep
print('\033[1;33m=-=' * 10)
print('Adivinhe um número de 0 a 5')
print('=-=' * 10, '\033[m')
nu = randint(0, 5)
a = int(input('\033[34mEscolha um número:\033[m '))
print('\033[7mCARREGANDO\033[m')
sleep(2)
if nu == a:
    print('\033[1;32mParabéns você Ganhou!\033[m')
else:
    print('\033[1;31mNão foi dessa vez. Eu escolhi {}\033[m'.format(nu))
