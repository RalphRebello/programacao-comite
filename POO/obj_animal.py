class Animal:
    def fazer_som(self):
        print('Fazendo som de animal')


class Gato(Animal):
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print('MIAU')


class Cachorro(Animal):
    def __init__(self, raca):
        self.raca = raca


def main():
    cachorro = Cachorro('Pitbull')
    cachorro.fazer_som()

    gato = Gato('Pantera')
    gato.fazer_som()


main()
