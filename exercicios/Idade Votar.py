def voto(nas):
    from datetime import date
    idade = date.today().year - nas
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: NÃO VOTA'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
