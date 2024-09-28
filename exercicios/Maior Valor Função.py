from time import sleep


def maior(*num):
    print('=-'*20)
    print('Analisando os valores informados...')
    sleep(1)
    maior = cont = 0
    for valor in num:
        print(valor, end=' ')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram os {cont} valores informados.')
    print(f'O maior valor entre eles é {maior}')


maior(1, 2, 4, 6, 1, 7)
maior(1, 9, 3, 6)
maior()
maior(3, 2)
