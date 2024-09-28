def notas(*nu, sit=False):
    """
    =-= Lê suas notas, calcula a média e diz sua situção =-=
    :param nu: Médias a serem lidas
    :param sit: (opcional) Situação em relação a média do aluno
    :return: Retorna com o dicionário das notas
    """
    lista = {'Total': len(nu), 'Maior': max(nu), 'Menor': min(nu), 'Média': sum(nu) / len(nu)}
    if sit:
        if lista['Média'] >= 8:
            lista['Situação'] = 'BOA'
        elif 6 < lista['Média'] < 8:
            lista['Situação'] = 'RAZOALVEL'
        elif 4 < lista['Média'] < 6:
            lista['Situação'] = 'PREOCUPAVEL'
        else:
            lista['Situação'] = 'REPROVADO'

    return lista


valores = notas(7, 7, 10, 7, 9, sit=True)
print(valores)
