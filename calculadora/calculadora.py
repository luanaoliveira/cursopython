# Utiliza dois "input" para receber 2 números de entrada e converte os valores recebidos
print("============= Calculadora =============")
print(' ')
number_1 = float(input("Digite o primeiro número: "))
number_2 = float(input("Digite o segundo número: "))

calculator = ('''
        
Escolha a operação que deseja realizar:

    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Potência
    6 - Sair

=======================================

''')

print(calculator)

# Adiciona um laço de repetição que permite ao usuário realizar várias operações consecutivaas
while True:
    option = float(input("Operação: "))
    if (option == 1):
        sum = number_1 + number_2
        print(' ')
        print(" Resultado da soma: ", round(sum, 2))
        print(' ')
    elif (option == 2):
        subtraction = number_1 - number_2
        print(' ')
        print(" Resultado da subtração: ", round(subtraction, 2))
        print(' ')
    elif (option == 3):
        multiplication = number_1 * number_2
        print(' ')
        print(" Resultado da multiplicação: ", round(multiplication, 2))
        print(' ')
    elif (option == 4):
        if number_2 == 0:
            print(' ')
            print(" Não é possível dividir por zero!")
            print(' ')
        else:
            division = number_1 / number_2
            integer_division = number_1 // number_2
            rest_of_division = number_1 % number_2
            print(' ')
            print(" Resultado da divisão: ", round(division, 2))
            print(" Divisão inteira: ", integer_division)
            print(" Resto da divisão: ", rest_of_division)
            print(' ')
    elif (option == 5):
        power= number_1 ** number_2
        print(' ')
        print(" Resultado da potência: ", round(power, 2))
        print(' ')
    elif (option == 6):
        print(' ')
        print("Saindo do programa...")
        print(' ')
        break
    else:
        print(' ')
        print(" Opção inválida! \n Por favor escolha uma operação válida.")
        print(' ')