def escreva(palavra):
    tam = len(palavra) + 4
    print('~'*tam)
    print(f'  {palavra:^}')
    print('~'*tam)


escreva('Olá,Mundo!')
escreva('Luiz Felipe 3ªA')
