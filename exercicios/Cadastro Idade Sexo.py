maiores = homens = mulheres20 = 0
while True:
    print('--'*10)
    print('Cadastre Uma Pessoa')
    print('--'*10)
    idade = int(input('Idade: '))
    sexo = quer = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    while quer not in 'SN':
        quer = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quer == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Temos {maiores} pessoas com mais de 18 anos.')
print(f'Ao todo são {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
