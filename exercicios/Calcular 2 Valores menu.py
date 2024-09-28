from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''\033[33mEscolha o que fazer com esses valores:
   1 - Somar.
   2 - Multiplicar.
   3 - O Maior valor.
   4 - Escolher novos números.
   5 - Encerrar programa.\033[m''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('\033[32mA soma entre os volores é {}'.format(n1 + n2))
    elif opcao == 2:
        print('\033[32mA multiplicação entre os voleres é {}'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('\033[32mO maior valor é {}'.format(n1))
        else:
            print('\033[32mO maior valor é {}'.format(n2))
    elif opcao == 4:
        print('\033[1mNovos números:\033[m')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('\033[3;31mEncerrando Programa.')
        sleep(1.5)
        print('Obrigado pela preferência!!')
        sleep(1)
        quit()
    else:
        print('\033[1mOpção Inválida.')
