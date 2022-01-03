"""
    Para o segundo exercício, você deve criar um programa que realize uma
    cópia do arquivo "alunos.csv". Essa cópia deve ser um arquivo chamado
    "alunos_copia.csv".
"""

from exec_1 import csv, ler_arq_csv


def cria_copia_csv(local_do_arquivo, novo_arquivo):

    with open(novo_arquivo, 'w', encoding='utf-8', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in ler_arq_csv(local_do_arquivo):
            escritor.writerow(linha)


cria_copia_csv('..\\alunos.csv', '..\\alunos_copia.csv')
