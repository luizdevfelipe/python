while True:
    nu = int(input('Qual tabuada deseja ver? '))
    print('=-=' * 10)
    if nu < 0:
        break
    for c in range(1, 11):
        print(f'{nu} X {c} = {nu * c}')
    print('=-=' * 10)
print('Programa Encerrado.')
