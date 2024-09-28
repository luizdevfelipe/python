print('-'*16)
print('LOJA VENDE TUDO')
print('-'*16)
compra = tot1000 = cont = valorbarato = 0
nomebarato = ''
while True:
    cont += 1
    produto = str(input('Nome do Produto: ')).strip()
    valor = float(input('Preço R$'))
    quer = ' '
    compra += valor
    if valor > 1000:
        tot1000 += 1
    if cont == 1 or valor < valorbarato:
        nomebarato = produto
        valorbarato = valor
    while quer not in 'SN':
        quer = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if quer == 'N':
        break
print('{:-^31}'.format(' FIM DO PROGRAMA '))
print(f'O valor total de suas compras foi R${compra:.2f}')
print(f'Temos {tot1000} produto(s) com valor acima de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custou R${valorbarato:.2f}')
