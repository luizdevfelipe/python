from math import sqrt


def linha(cor):
    print(f'{cores[cor]}-'*42, cores['sem'])


cores = {'sem': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m',
         'azul': '\033[1;34m', 'negrito': '\033[1m', 'cinza': '\033[1;37m', 'roxo': '\033[1;35m',
         'teste': '\033[1;30;42m'
         }


def cabecalho(msg, cor='sem'):
    total = 42
    print(f'{cores[cor]}-' * total, cores['sem'])
    print(f'{cores[cor]} {msg:^41} {cores["sem"]}')
    print(f'{cores[cor]}-' * total, cores['sem'])


def LeiaStr(msg):
    while True:
        try:
            palavra = str(input(msg))
        except(SyntaxError, IndexError):
            print(f'\033[1mERRO! Digite apenas palavras\033[m')
        else:
            return palavra


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
            n = str(input(msg)).replace(',', '.')
            if n.isalpha() or n == '':
                print('\033[31mERRO! Digite um número decimal válido.\033[m')
                continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar um valor.\033[m')
            return 0
        else:
            return float(n)


def opcao(ini, fim):
    inicio = ini - 1
    while True:
        leia_escolha = LeiaInt('Sua escolha: ')
        if inicio < leia_escolha <= fim:
            return leia_escolha
        else:
            print(f'\033[31mERRO! Escolha uma opção entre {ini} a {fim}\033[m')


# CóDiGo PrInCiPaL

while True:
    cabecalho('ESCOLHA SUA CALCULADORA', 'teste')

    cabecalho('''
    0 - ❌ ENCERRAR ❌
    1 - Contas Básicas
    2 - IMC
    3 - Regra de Três
    4 - Delta
    5 - Fatorial
    6 - Conversor Medidas
    ''', 'amarelo')

    escolha = opcao(0, 6)

    if escolha == 0:
        cabecalho('FINALIZADO', 'cinza')
        break

    elif escolha == 1:
        cabecalho('''
        0 - 🔙 RETORNAR
        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        ''', 'azul')

        contas = opcao(0, 4)
        if contas == 0:
            cabecalho('VOLTANDO', 'cinza')
        else:
            linha('amarelo')
            n1 = LeiaFloat('\033[1;33mPrimeiro Termo: ')
            n2 = LeiaFloat('Segundo Termo:\033[m ')
            linha('amarelo')
            if contas == 1:
                res = n1 + n2
                cabecalho(f'O Resultado é {res:.2f}', 'negrito')
            elif contas == 2:
                res = n1 - n2
                cabecalho(f'O Resultado é {res:.2f}', 'negrito')
            elif contas == 3:
                res = n1 * n2
                cabecalho(f'O Resultado é {res:.2f}', 'negrito')
            else:
                res = n1 / n2
                cabecalho(f'O Resultado é {res:.2f}', 'negrito')

    elif escolha == 2:
        linha('amarelo')
        peso = LeiaFloat('\033[1;33mDigite o Peso: ')
        altura = LeiaFloat('Digite sua Altura:\033[m ')
        imc = peso / (altura ** 2)
        linha('amarelo')
        cabecalho(f'O Resultado do seu IMC foi {imc:.1f}', 'negrito')

        if imc < 18.5:
            print(f'{cores["roxo"]}É classificado como abaixo do peso.{cores["sem"]}')
        elif imc <= 25:
            print(f'{cores["roxo"]}É classificado como peso ideal.{cores["sem"]}')
        elif imc <= 30:
            print(f'{cores["roxo"]}É classificado como sobrepeso.{cores["sem"]}')
        elif imc <= 40:
            print(f'{cores["roxo"]}É classificado como obesidade.{cores["sem"]}')
        else:
            print(f'{cores["roxo"]}É classificado como obesidade mórbida.{cores["sem"]}')
        linha('negrito')

    elif escolha == 3:
        cabecalho('''   ORDEM:
            1º === 2º
            3º === X''', 'azul')
        linha('amarelo')
        primeiro_v = LeiaFloat('\033[1;33mPrimeiro Valor: ')
        segundo_v = LeiaFloat('Segundo Valor: ')
        terceiro_v = LeiaFloat('Terceiro Valor:\033[m ')
        linha('amarelo')
        mult = segundo_v * terceiro_v
        valor_f = mult / primeiro_v
        cabecalho(f'O resultado de X é {valor_f:.2f}', 'negrito')

    elif escolha == 4:
        linha('amarelo')
        a = LeiaInt('\033[1;33mValor de A = ')
        b = LeiaInt('Valor de B = ')
        c = LeiaInt('Valor de C = \033[m')
        linha('amarelo')

        Delta = b ** 2 - 4 * a * c
        try:
            raiz = sqrt(Delta)
            print(f'\033[34mDelta = {Delta:.2f}\033[m')
            print(f'\033[34mRaiz do Delta = {raiz:.2f}\033[m')
            x1 = (-b + raiz) / (2 * a)
            x2 = (-b - raiz) / (2 * a)
            cabecalho(f'''  Resultado:            
        x\' = {x1:.2f}
        x\" = {x2:.2f}''', 'negrito')
        except ValueError:
            print('\033[1;31mNão foi possível calcular o resultado do delta.\033[m')

    elif escolha == 5:
        linha('amarelo')    # 2  x 1 x 0... x 3 x 2 x 1 = 2
        nu = LeiaInt('\033[1;33mDigite um número: ')
        if nu > 110:
            print('\033[1;31mERRO! Digite um valor menor ou igual a 110!\033[m')
        while not nu <= 110:
            nu = LeiaInt('\033[1;33mDigite um número: ')
            if nu > 110:
                print('\033[1;31mERRO! Digite um valor menor ou igual a 110!\033[m')
        p_nu = nu
        f = 1
        linha('amarelo')
        print(f'\033[1;32mO resultado do número {nu}\033[m')
        while nu > 0:
            f *= nu
            nu -= 1
        print(f'\033[1;34m{p_nu} x {p_nu - 1} x {p_nu - 2}... x 3 x 2 x 1 = ', end='')
        print(f)

    elif escolha == 6:

        cabecalho('''
        0 - 🔙 RETORNAR
        1 - Conversor de Líquidos
        2 - Conversor de Velocidade
        ''', 'azul')
        conversor = opcao(0, 2)

        if conversor == 0:
            cabecalho('VOLTANDO', 'cinza')

        elif conversor == 1:
            cabecalho('''
            1 - De M³ para Litros
            2 - de Litros para M³
            ''', 'azul')
            opc = opcao(1, 2)
            nu = LeiaInt('Digite o valor: ')
            if opc == 1:

                cabecalho(f'O valor {nu}m³ equivale à {nu * 1000}l.', 'negrito')

            elif opc == 2:

                cabecalho(f'O valor {nu}L equivale à {nu / 1000}m³', 'negrito')

        elif conversor == 2:
            linha('amarelo')
            vel_1 = LeiaInt('Velocidade 1: ')







