n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O \033[7mPrimeiro\033[m valor é maior.')
elif n1 < n2:
    print('O \033[7mSegundo\033[m valor é maior.')
else:
    print('Os valores são \033[7mIguais.\033[m')
