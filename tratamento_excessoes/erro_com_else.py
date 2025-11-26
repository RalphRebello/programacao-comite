def obtem_valor():
    try:
        valor = float(input('Informe um numero -> '))
    except ValueError:
        print('Valor inválido!', end=' ')
        print('Necessário ser um numero inteiro!')
    else:
        print(f'Valor informado é {valor}')
        return int(input('Informe um valor -> '))


def main():
    obtem_valor()


main()
