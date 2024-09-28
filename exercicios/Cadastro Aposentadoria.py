from datetime import date
pessoa = dict()
pessoa['Seu nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
pessoa['Sua idade'] = date.today().year - ano
trabalho = str(input('É registrado? '))
if trabalho in 'sS':
    cont = int(input('Em que ano foi contratado? '))
    pessoa['Seu salário'] = float(input('Seu salário R$'))
    pessoa['Sua idade de aposentadoria'] = (35 - (date.today().year - cont)) + pessoa['Sua idade']
print('=-'*20)
print('   -= INFORMAÇÕES =-')
for k, v in pessoa.items():
    print(f'    {k} é {v}')
print('=-'*20)
