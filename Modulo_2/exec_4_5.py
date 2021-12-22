"""
    Crie um dicionário cujas chaves são os meses do ano e os valores são a
    duração (em dias) de cada mês.
"""

meses_2022 = {
    'Janeiro': 31,
    'Fevereiro': 28,
    'Março': 31,
    'Abril': 30,
    'Maio': 31,
    'Junho': 30,
    'Julho': 31,
    'Agosto': 31,
    'Setembro': 30,
    'Outubro': 31,
    'Novembro': 30,
    'Dezembro': 31
}

"""
    Imprima as chaves seguidas dos seus valores para dicionário criado no
    exercício anterior.
    Exemplo:
    Janeiro - 31
    Fevereiro - 28
    Março - 31
    Etc...
"""
for k, v in meses_2022.items():
    print(f'{k:9} - {v} dias')