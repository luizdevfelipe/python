pessoa = dict()
cadastrados = list()
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo: '))[0].upper()
        if pessoa['sexo'] not in 'FM':
            print('Digite Novamente [M/F].')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastrados.append(pessoa.copy())
    while True:
        quer = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if quer not in 'SN':
            print('Digite Novamente [S/N]')
        else:
            break
    if quer == 'N':
        break
print('=-'*20)
print(f'Foram cadastradas {len(cadastrados)} pessoas.')
if len(cadastrados) > 1:
    media = soma / len(cadastrados)
    print(f'A média das idades foi de {media:.1f} anos')
    for m in cadastrados:
        if m['sexo'] in 'F':
            print('As mulheres foram ', end='')
            for p in cadastrados:
                if p['sexo'] == 'F':
                    print(f'[{p["nome"]}]', end=' ')
            print()
    if 1 < len(cadastrados) < 3:
        print('A pessoa com maior idade é ', end='')
    else:
        print('As pessoas com idade acima da média são ', end='')
    for p in cadastrados:
        if p['idade'] > media:
            print(f'[{p["nome"]}]', end=' ')
    print()
else:
    print(f'{pessoa["nome"]} foi o(a) único(a) cadastrado(a).')
