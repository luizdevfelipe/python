from datetime import date
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - nascimento
print('Sua idade é de {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria \033[7mMirim.\033[m')
elif idade <= 14:
    print('Você está na categoria \033[7mInfantil.\033[m')
elif idade <= 19:
    print('Você está na categoria \033[7mJunior.\033[m')
elif idade == 20:
    print('Você está na categoria \033[7mSênior.\033[m')
else:
    print('Você está na categoria \033[7mMaster.\033[m')
