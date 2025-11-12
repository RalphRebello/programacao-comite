def remover_repetidos(lista_numeros):
    lista_unicos = set(lista_numeros)
    return lista_unicos


def main():
    lista_numeros = [1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 9, 9, 9]
    resultado = remover_repetidos(lista_numeros)

    for i in resultado:
        print(i, end=' ')

    print()


main()
