def obtem_valor():
    try:
        valor = int(input('Informe um valor inteiro -> '))
    except ValueError:
        print('Valor inválido!', end=' ')
        print('Necessário ser um numero inteiro!')
    else:
        print(f'Valor informado é {valor}')
    finally:
        print('PROGRAMA ENCERRADO!')


def main():
    obtem_valor()


main()
