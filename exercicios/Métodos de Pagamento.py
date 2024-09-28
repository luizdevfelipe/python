valor = float(input('Digite o valor do produto: '))
print('''\033[33mEscolha a opção de pagamento: 
1 - À vista no Dinheiro ou Cheque, 10% de desconto.
2 - À vista no Cartão, 5% de desconto.
3 - 2x no Cartão, preço normal.
4 - 3x ou mais no Cartão, 20% de juros.\033[m''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('\033[32mÀ vista no dinheiro/cheque o valor será R${:.2f}'.format(valor - (valor * 0.10)))
elif escolha == 2:
    print('\033[32mÀ vista no cartão o valor será R${:.2f}'.format(valor - (valor * 0.05)))
elif escolha == 3:
    print('\033[32m2x no cartão o valor será R${:.2f}'.format(valor))
elif escolha == 4:
    print('\033[32m3x ou mais no cartão o valor será de R${}'.format(valor + (valor * 0.20)))
else:
    print('Opção não encontrada.')
