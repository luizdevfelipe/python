quero = ''
cont = nu = maior = menor = 0
while quero != 'n':
    nu = int(input('Digite um número: '))
    quero = str(input('Quer continuar? [S/N] ')).strip()[0].lower()
    cont += 1
    if cont == 1:
        maior = menor = nu
    else:
        if nu > maior:
            maior = nu
        if nu < menor:
            menor = nu
print('Você digitou {} número e a média entre eles foi {}'.format(cont, (nu + nu) / cont))
print('O maior número é {} e o menor é {}'.format(maior, menor))
