"""
    Finalmente chegamos ao último exercício dessa sequência relacionada à
    manipulação de arquivos.

    Neste exercício você deve criar um novo arquivo chamado "alunos_media.csv".
    Esse novo arquivo é uma cópia de "alunos.csv" porém com uma coluna a mais
    chamada "Média" que vai abrigar os valores das médias das provas de cada aluno da lista.
"""

from exec_2 import csv, ler_arq_csv, cria_copia_csv


def media_de_notas_csv(local_arquivo, novo_arquivo):

    arquivo_lido = ler_arq_csv(local_arquivo)

    soma = 0
    media = 0.0
    for linha in arquivo_lido[1:]:
        for nota in linha[3:]:
            soma += float(nota)
        media = soma / len(linha[3:])
        soma = 0
        print(f'{media:.2f}')


media_de_notas_csv('..\\alunos.csv', None)