nu = int(input('Digite um número: '))
print('''Escolha uma das opções:
\033[33m1 Para Binário
2 Para Octal
3 Para Hexadecimal\033[m''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('\033[32mO número {} em Binário é {}'.format(nu, bin(nu)[2:]))
elif opcao == 2:
    print('\033[32mO número {} em Octal é {}'.format(nu, oct(nu)[2:]))
elif opcao == 3:
    print('\033[32mO número {} em Hexadecimal é {}'.format(nu, hex(nu)[2:]))
else:
    print('\033[1;31mOpção não encontrada.')
