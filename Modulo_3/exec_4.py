"""
    Você conhece Star Wars? Se trata, obviamente, da famosa saga espacial
    criada por George Lucas em 1977 e que deu origem a símbolos do cinema e
    da cultura pop com o imponente vilão Darth Vader ou o simpático robô
    R2-D2. A ideia desse exercício é justamente extrair informações do
    personagem Darth Vader através de uma API de Star Wars chamada SWAPI.

    Utilize a URL "https://swapi.dev/api/people/4/" para fazer a requisição dos
    dados de Darth Vader e extraia as informações "name" (nome), "height"
    (altura), "mass" (massa) e "birth_year" (ano de nascimento) e imprima cada
    dado em uma linh
"""

from requests import get


url = 'https://swapi.dev/api/people/4/'

requisicao = get(url)

dados = requisicao.json()

for k, v in dados.items():
    if k == 'name' or k == 'height' or k == 'mass' or k == 'birth_year':
        print(f'{k}: {v}')