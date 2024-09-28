aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*15)
print(f'Nome do aluno(a) é {aluno["nome"]}')
print(f'Sua média foi de {aluno["media"]} pontos.')
if aluno['media'] >= 7:
    print(f'{aluno["nome"]} foi Aprovado')
elif 5 <= aluno['media'] < 7:
    print(f'{aluno["nome"]} está em Recuperação')
else:
    print(f'{aluno["nome"]} foi Reprovado')
