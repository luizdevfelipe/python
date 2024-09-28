completa = list()
par = list()
impar = list()
while True:
    completa.append(int(input('Digite um valor: ')))
    quer = str(input('Quer Continuar? [S/N] '))
    if quer in 'Nn':
        break
for i, v in enumerate(completa):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('='*60)
print(f'Você digitou os seguintes valores: {completa}')
print(f'OS valores pares são {par}')
print(f'Os valores ímpares são {impar}')
