def contar_positivos(l_numeros):

    cont_positivos = 0

    for numero in l_numeros:
        if numero > 0:
            cont_positivos += 1

    print(f'Na lista existem {cont_positivos} '
          'numeros positivos')


def main():
    lista_numeros = [3, 6, 4, -9, -7, -6, 3, 4, 1, 19]
    contar_positivos(lista_numeros)


main()
