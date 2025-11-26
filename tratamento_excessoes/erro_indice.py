from random import randint


def gerar_lista():
    lista = []
    for i in range(randint(1, 30)):
        lista.append(randint(1, 100))
    return lista


def ler_lista(lista):
    for i in lista:
        print(i, end=' ')


def main():
    lista = gerar_lista()
    ler_lista(lista)
    try:
        print('\nIndice 15 ->', lista[15])
    except IndexError:
        print('\nValor não foi gerado!')
    print()


main()
