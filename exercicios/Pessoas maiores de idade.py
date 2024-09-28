from datetime import date
hoje = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nasceu = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = hoje - nasceu
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Dessas pessoas \033[32m{} são Maiores\033[m e \033[31m{} são Menores.'.format(maiores, menores))
