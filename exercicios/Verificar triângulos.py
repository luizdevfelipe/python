print('\033[33m=-='*10)
print('Verificar Triângulos v2.0')
print('=-='*10)
a = float(input('\033[mPrimeiro Valor: '))
b = float(input('Segundo Valor: '))
c = float(input('Terceiro Valor: '))
if a < b + c and b < a + c and c < a + b:
    print('Com esse valores É possivel formar um triângulo ', end='')
    if a == b == c:
        print('Equilátero.')
    elif a != b != c != a:
        print('Escaleno.')
    else:
        print('Isóceles.')
else:
    print('Com esses valores Não é possivel formar um triângulo.')
