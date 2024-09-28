from datetime import date
ano = int(input('Digite o ano, ou digite 1 para calcular seu ano atual: '))
if ano == 1:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} Não é Bissexto.'.format(ano))




