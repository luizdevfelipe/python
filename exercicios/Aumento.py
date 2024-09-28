print('<<<< Aumento de Salários v1.0 >>>>')
sa = float(input('Qual o salário do funcionário? R$'))
au = sa * 0.15
print("Um funcionário que ganha R${}, com o aumento de 15% passa a ganhar R${:.2f}.".format(sa, au + sa))
