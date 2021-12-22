"""
    Faça uma função que recebe duas listas e retorna a soma item a item dessas
    listas.
    Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
    retornar [1+3, 4+5, 3+1] = [4, 9, 4].
"""


def soma_lista(lista_1, lista_2):
    return [n1 + n2 for n1, n2 in zip(lista_1, lista_2)]

