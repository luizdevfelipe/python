print('''\033[34m===== Conversor de Volume =====
1 - De M³ para Litros
2 - de Litros para M³\033[m''')
while True:
    nu = int(input('Digite o valor: '))
    opcao = int(input('Sua opção: '))
    while 0 < opcao > 2:
        opcao = int(input('\033[3mDigite novamente sua opção:\033[m '))
    if opcao == 1:
        print('-'*30)
        print(f'O valor {nu}m³ passa para {nu*1000}l.')
        print('-' * 30)
    elif opcao == 2:
        print('-'*30)
        print(f'O valor {nu}L passa para {nu/1000}m³')
        print('-' * 30)
    parar = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if parar == 'N':
        break
print('\033[1m='*30)
print('Programa Finalizado.')
