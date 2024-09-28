cont = soma = 0
while True:
    nu = int(input('Digite um número [999 Stop]: '))
    if nu == 999:
        break
    cont += 1
    soma += nu
print(f'Foram digitados {cont} números e a soma foi de {soma}')
