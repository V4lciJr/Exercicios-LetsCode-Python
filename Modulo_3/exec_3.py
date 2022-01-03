"""
    Finalmente chegamos ao último exercício dessa sequência relacionada à
    manipulação de arquivos.

    Neste exercício você deve criar um novo arquivo chamado "alunos_media.csv".
    Esse novo arquivo é uma cópia de "alunos.csv" porém com uma coluna a mais
    chamada "Média" que vai abrigar os valores das médias das provas de cada aluno da lista.
"""

from exec_2 import csv, ler_arq_csv


def media_de_notas_csv(local_arquivo, novo_arquivo):

    arquivo_lido = ler_arq_csv(local_arquivo)

    soma = 0
    lista_media = ['media']
    for linha in arquivo_lido[1:]:
        for nota in linha[3:]:
            soma += float(nota)
        media = soma / len(linha[3:])
        lista_media.append(f'{media:.2f}')
        soma = 0

    with open(f'..\\{novo_arquivo}', 'w', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        for i in range(0, len(arquivo_lido)):
            arquivo_lido[i].append(lista_media[i])
            escritor.writerow(arquivo_lido[i])


media_de_notas_csv('..\\alunos.csv', 'alunos_media.csv')
