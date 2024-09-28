from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
sexo = str(input('Digite seu sexo: ')).strip().lower()
pc = date.today().year
idade = pc - ano
if sexo == 'feminino':
    print('\033[1;32mVocê é mulher não precisa se alistar!\033[m')
    quit()
elif idade < 18:
    print('\033[1;32mEm {} você tem {} anos.'.format(pc, idade))
    print('Você ainda vai se alistar, falta(m) {} ano(s).'.format(18 - idade))
    print('Você se alistará em {}.\033[m'.format((18 - idade) + pc))
elif idade == 18:
    print('\033[1;33mEm {} você tem {} anos.'.format(pc, idade))
    print('Este é o ano para se alistar.\033[m')
else:
    print('\033[1;31mEm {} você tem {} anos.'.format(pc, idade))
    print('Já se passou {} ano(s) da data de seu alistamento.'.format(idade - 18))
    print('Você deviria ter se alistado em {}.\033[m'.format(ano + 18))
