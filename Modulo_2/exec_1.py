"""
    Faça um programa que olhe todos os itens de uma lista e diga quantos deles
    são pares.
"""


def cont_pares(lista):
    cont = 0
    try:
        for n in lista:
            if n % 2 == 0:
                cont += 1

        return cont
    except TypeError:
        return 'Sua lista não possui apenas números inteiros'
