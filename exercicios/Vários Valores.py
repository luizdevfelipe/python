nu = cont = soma = 0
while nu != 999:
    nu = int(input('Digite um número inteiro [999 Stop]: '))
    cont += 1
    soma += nu
print('\033[32mForam digitados {} números e a soma foi de {}'.format(cont - 1, soma - 999))
