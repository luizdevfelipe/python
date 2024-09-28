totidade = 0
mulheres = 0
nomehomem = ''
homemvelho = 0
for p in range(1, 5):
    print('\033[1;33m--- {}ªPessoa ---\033[m'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    totidade += idade
    if p == 1 and sexo == 'm':
        homemvelho = idade
        nomehomem = nome
    if sexo == 'm' and idade > homemvelho:
        homemvelho = idade
        nomehomem = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1
print('A média de idade do grupo é de {} anos.'.format(totidade / 4))
print('A idade do homem mais velho é {} anos e ele se chama {}.'.format(homemvelho, nomehomem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres))
