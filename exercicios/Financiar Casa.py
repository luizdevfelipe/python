casa = float(input('Qual o valor da casa R$'))
salario: float = float(input('Qual seu salário R$'))
anos = float(input('Em quantos anos vai pagar as parcelas R$'))
parcelas = casa / (anos * 12)
porcent = salario * 0.30
if parcelas <= porcent:
    print('\033[1;32mSeu empréstimo foi aprovado! suas parcelas serão de R${:.2f}\033[m'.format(parcelas))
else:
    print('\033[1;31mSeu empréstimo foi negado! As parcelas foram de ', end='')
    print('R$10{:.2f} e excederam 30% do seu salário.\033[m'.format(parcelas))

