"""
    Vamos fazer um programa para verificar quem é o assassino de um crime.
    Para descobrir o assassino, a polícia faz um pequeno questionário com 5
    perguntas onde a resposta só pode ser sim ou não:

    a. Mora perto da vítima?
    b. Já trabalhou com a vítima?
    c. Telefonou para a vítima?
    d. Esteve no local do crime?
    e. Devia para a vítima?

    Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
    suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
    2 pontos são apenas suspeitos, necessitando outras investigações. Valores
    iguais ou abaixo de 1 são liberados.
"""
print('Todas as perguntas desse interrogatório devem ser respondidas somente com Sim ou Não.')

pontos = 0
perguntas = ['Você mora perto da vítima ', 'Você já trabalhou com a vítima', 'Telefonou para a vítima',
             'Você esteve no local do crime ', 'Você devia alguma coisa para a vítima']

for pergunta in perguntas:
    resp = input(f'{pergunta}, Sim ou Não? ')
    if resp.lower() == 'sim':
        pontos += 1

if pontos > 4:
    veredito = f'Você obteve {pontos} pontos no interrogatório, o que conclui é que você é o assassino desse caso'
elif pontos > 2:
    veredito = f'Você obteve {pontos} pontos no interrogatório, o que conclui é que você é cúmplice do assassino'
elif pontos > 1:
    veredito = f'Você obteve {pontos} pontos no interrogatório, uma pontuação baixa, mesmo assim você ainda é um ' \
               f'suspeito '
else:
    veredito = f'Você obteve {pontos} pontos no interrogatório, e é inocente, tá liberado.'

print(veredito)