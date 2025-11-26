def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print('O divisor não pode ser 0')
    else:
        print(f'Valor da divisão: {resultado}')


def obtem_valores():
    a = int(input('Informe o primeiro valor -> '))
    b = int(input('Informe o segundo valor -> '))

    dividir(a, b)


def main():
    obtem_valores()


main()
