def obtem_valor():
    return int(input('Informe um valor -> '))


def main():
    try:
        valor = obtem_valor()
    except ValueError:
        print('Valor inválido!', end=' ')
        print('Necessário ser um numero inteiro!')
    else:
        print(f'Valor informado é {valor}')


main()
