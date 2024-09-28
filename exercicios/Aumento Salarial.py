nu = float(input('Digite seu salário: '))
if nu <= 1250:
    print('Seu salário é de R${} teve um aumento de 15% e passou a R${:.2f}'.format(nu, (nu * 0.15) + nu))
else:
    print('Seu salário é de R${} teve um aumento de 10% e passou a R${:.2f}'.format(nu, (nu * 0.10) + nu))
print('Aproveite seu aumento.')
