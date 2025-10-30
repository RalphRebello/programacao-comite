def pares(lista_numeros):

    lista_pares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)

    return lista_pares


def main():
    lista_numeros = [3, 5, 6, 3, 1, 2, 4, 6, 8, 6, 9]
    lista_final = pares(lista_numeros)

    for n in lista_final:
        print(n, end=' ')
    print()


main()
