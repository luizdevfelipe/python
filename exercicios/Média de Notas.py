nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2) / 2
print('Sua média foi {:.1f}'.format(media))
if media < 5:
    print('\033[1;31mO aluno foi Reprovado.')
elif 5 <= media < 7:
    print('\033[1;33mO aluno está em Recuperação.')
elif media >= 7:
    print('\033[1;32mO aluno foi Aprovado.')
