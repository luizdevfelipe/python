from math import sqrt


def operacoes_matematicas():
    print('''
    0 - 🔙 RETORNAR
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    ''')
    contas = opcao(0, 4)
    if contas == 0:
        print('VOLTANDO')
    else:
        n1 = leia_float('Primeiro Termo: ')
        n2 = leia_float('Segundo Termo: ')
        if contas == 1:
            res = n1 + n2
            print(f'O Resultado é {res:.2f}')
        elif contas == 2:
            res = n1 - n2
            print(f'O Resultado é {res:.2f}')
        elif contas == 3:
            res = n1 * n2
            print(f'O Resultado é {res:.2f}')
        else:
            res = n1 / n2
            print(f'O Resultado é {res:.2f}')


def indice_corporal():
    peso = leia_float('Digite o Peso: ')
    altura = leia_float('Digite sua Altura: ')
    imc = peso / (altura ** 2)
    print(f'O Resultado do seu IMC foi {imc:.1f}')

    if imc < 18.5:
        print('É classificado como abaixo do peso.')
    elif imc <= 25:
        print('É classificado como peso ideal.')
    elif imc <= 30:
        print('É classificado como sobrepeso.')
    elif imc <= 40:
        print('É classificado como obesidade.')
    else:
        print('É classificado como obesidade mórbida.')


def regra_tres():
    print('''   ORDEM:
        1º === 2º
        3º === X''')
    primeiro_v = leia_float('Primeiro Valor: ')
    segundo_v = leia_float('Segundo Valor: ')
    terceiro_v = leia_float('Terceiro Valor: ')
    mult = segundo_v * terceiro_v
    valor_f = mult / primeiro_v
    print(f'O resultado de X é {valor_f:.2f}')


def delta():
    a = leia_int('Valor de A = ')
    b = leia_int('Valor de B = ')
    c = leia_int('Valor de C = ')

    result = b ** 2 - 4 * a * c
    try:
        raiz = sqrt(result)
        print(f'Delta = {result:.2f}')
        print(f'Raiz do Delta = {raiz:.2f}')
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print(f'''  Resultado:            
    x\' = {x1:.2f}
    x\" = {x2:.2f}''')
    except ValueError:
        print('Não foi possível calcular o resultado do delta.')


def fatorial():
    valor = 111
    while not valor <= 110:
        valor = leia_int('Digite um número: ')
        if nu > 110:
            print('ERRO! Digite um valor menor ou igual a 110!')
    p_nu = valor
    f = 1
    while valor > 0:
        f *= valor
        valor -= 1
    print(f'O fatorial de {p_nu} é {f}')


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, SyntaxError):
            print('ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar um valor.')
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = str(input(msg)).replace(',', '.')
            if n.isalpha() or n == '':
                print('ERRO! Digite um número decimal válido.')
                continue
        except KeyboardInterrupt:
            print('\nO usuário preferiu não informar um valor.')
            return 0
        else:
            return float(n)


def opcao(ini, fim):
    while True:
        leia_escolha = leia_int('Sua escolha: ')
        if ini <= leia_escolha <= fim:
            return leia_escolha
        else:
            print(f'ERRO! Escolha uma opção entre {ini} a {fim}')


# CóDiGo PrInCiPaL =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

while True:
    print('\n     ESCOLHA SUA CALCULADORA')

    print('''
    0 - ❌ ENCERRAR ❌
    1 - Contas Básicas
    2 - IMC
    3 - Regra de Três
    4 - Delta
    5 - Fatorial
    6 - Conversor Medidas
    ''')

    escolha = opcao(0, 6)

    if escolha == 0:
        print('\n     FINALIZADO')
        break

    elif escolha == 1:
        operacoes_matematicas()

    elif escolha == 2:
        indice_corporal()

    elif escolha == 3:
        regra_tres()

    elif escolha == 4:
        delta()

    elif escolha == 5:
        fatorial()

    elif escolha == 6:

        print('''
        0 - 🔙 RETORNAR
        1 - Conversor de Líquidos
        2 - Conversor de Velocidade
        ''')
        conversor = opcao(0, 2)

        if conversor == 0:
            print('VOLTANDO', 'cinza')

        elif conversor == 1:
            print('''
            1 - De M³ para Litros
            2 - de Litros para M³
            ''')
            opc = opcao(1, 2)
            nu = leia_int('Digite o valor: ')
            if opc == 1:

                print(f'O valor {nu}m³ equivale à {nu * 1000}l.')

            elif opc == 2:

                print(f'O valor {nu}L equivale à {nu / 1000}m³')

        elif conversor == 2:
            vel_1 = leia_int('Velocidade 1: ')
