while True:

    numero = int(input('Digite o número que deseja saber a tabuada? '))

    for n in range(1, 11):
        print(f'{numero} x {n: >2} = {numero * n: 2}')

    resp = input('Deseja saber a tabuada de outros número ? [S/N] ')
    if resp.lower() == 'n':
        break
