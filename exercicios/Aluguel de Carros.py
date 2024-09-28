print('<<<< Aluguel de Carros v1.0 >>>>')
km = int(input('Quilômetros rodados '))
dia = int(input('Dias com o carro '))
pdia = dia * 60
pkm = km * 0.15
print('O valor a ser pago pelo aluguel do carro é R${:.2f}'.format(pdia + pkm))
