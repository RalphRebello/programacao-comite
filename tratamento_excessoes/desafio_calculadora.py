def obtem_operacao():
    n1, op, n2 = input('Insira a conta -> ')
    return n1, op, n2


def calcular():
    n1, op, n2 = obtem_operacao()
    try:
        if op == '+':
            print(n1, op, n2, '=', int(n1)+int(n2), '\n')
        elif op == '-':
            print(n1, op, n2, '=', int(n1)-int(n2), '\n')
        if op == '*':
            print(n1, op, n2, '=', int(n1)*int(n2), '\n')
        if op == '/':
            try:
                print(n1, op, n2, '=', int(n1)/int(n2), '\n')
            except ZeroDivisionError:
                print('Impossível dividir por zero!\n')
    except ValueError:
        print('Valor inserido é inválido!\n')


def menu():
    print('CALCULADORA')
    while True:
        try:
            opcao = input(f'Pressione 1 para calcular\n'
                          'Digite "sair" para encerrar\n\n'
                          '-> ')
            if opcao == 'sair':
                break
            elif opcao == '1':
                calcular()
            else:
                print(opcao, 'Opção inválida!\n')
                continue
        except Exception as erro:
            print(erro)


def main():
    menu()


main()
