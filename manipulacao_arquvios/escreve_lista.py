def gera_lista(lista):
    for i in range(5):
        fruta = input('Insira uma fruta -> ')
        lista.append(fruta)
    return lista


def escrever_frutas(lista):
    with open('frutas.txt', 'w') as arquivo:
        for fruta in lista:
            arquivo.write(fruta + '\n')
        print('Arquivo Gerado!')


def main():
    lista = []
    lista = gera_lista(lista)
    escrever_frutas(lista)


main()
