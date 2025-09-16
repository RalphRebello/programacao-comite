n1 = float(input("informe o primeiro valor -> "))
n2 = float(input("informe o segundo valor -> "))
op = input("Qual a operação? | + | - | * | / | -> ")

if op == '+':
    print(f'Soma: {n1} + {n2} = {n1 + n2}')
elif op == '-':
    print(f'Subtração: {n1} - {n2} = {n1 - n2}')
elif op == '*':
    print(f'Multiplicação: {n1} * {n2} = {n1 * n2}')
elif op == '/':
    if n2 != 0:
        print(f'Divisão: {n1} / {n2} = {n1 / n2}')
    else:
        print("impossível realizar uma divisão por 0")
else:
    print("Operação inválida! "
          "\nNecessário escolher uma das operações "
          "disponíveis: | + | - | * | / |")
