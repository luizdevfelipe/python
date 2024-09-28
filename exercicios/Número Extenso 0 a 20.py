extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
                                                                                            'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')
while True:
    nu = int(input('Digite um número de 0 a 20: '))
    if 0 <= nu <= 20:
        print(f'\033[32mVocê digitou o número {extenso[nu]}\033[m')
        opcao = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
        if opcao == 'N':
            break
    else:
        print('\033[3mTente novamente.\033[m')
print('\033[1mPrograma Encerrado\033[m')
