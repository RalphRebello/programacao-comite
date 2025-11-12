def calculadora(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            print('Divisão por 0! ')
        else:
            print(n1, n2)
            return n1 / n2


def main():
    continuar = True
    while continuar:
        numero1 = float(input('Informe o primeiro valor -> '))
        numero2 = float(input('Informe o segundo valor -> '))
        operacao = input('Informe a operação -> ')

        resultado = calculadora(numero1, numero2, operacao)
        if resultado != None:
            print(f'{numero1} {operacao} {numero2} = {resultado}')

        continuar = input('Deseja continuar? "S" ou "N" -> ')
        if continuar == 'S':
            continuar = True
        elif continuar == 'N':
            continuar = False
        else:
            print('Opção inválida!')
            continue


main()
