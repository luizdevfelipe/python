print('<<<< Calcular descontos v1.0 >>>>')
nu = float(input('Qual o valor do produto? R$'))
des = nu * 0.05
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}".format(nu, nu - des))