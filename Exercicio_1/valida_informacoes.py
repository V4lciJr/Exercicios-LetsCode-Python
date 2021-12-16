"""
    Faça um programa que leia a validade das informações:
    a. Idade: entre 0 e 150;
    b. Salário: maior que 0;
    c. Sexo: M, F ou Outro;

    O programa deve imprimir uma mensagem de erro para cada informação inválida.
"""
salario = 0
idade = 0
sexo = ''
while True:
    idade = int(input("Digite sua idade: "))
    if 0 < idade <= 150:
        break
    print("Idade invalida, por favor digite uma idade válida entre 0 e 150.")

while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    print("Salário inválido, por favor digite um valor válido maior que 0.")

while True:
    sexo = input("Digite seu sexo: ")
    if sexo.upper() == 'M' or sexo.upper() == 'F' or sexo.capitalize() == 'Outro':
        break
    print("Sexo inválido.")

print(f"Sua idade: {idade}\nSeu Salário: R${salario: .2f}\nSeu Sexo: {sexo.upper()}")