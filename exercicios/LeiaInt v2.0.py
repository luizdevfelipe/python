def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, SyntaxError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar um valor.\033[m')
            return 0
        else:
            return n


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, SyntaxError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar um valor.\033[m')
            return 0
        else:
            return n


nu = LeiaInt('Digite um número Inteiro: ')
nu2 = LeiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {nu} e o número real {nu2}')
