"""
Faça um programa que peça um valor monetário e diminua-o em 15%.
Seu programa deve imprimir a mensagem "O novo valor é [valor]".
"""

while True:
    value = float(input("Digite o valor que deseja diminuir 15%: "))
    value -= value * 0.15
    print(f'O novo valor é[R${value: .2f}]')

    resp = input('Deseja continuar com mais valores? [y/n] ')
    if resp.lower() == 'y':
        break
