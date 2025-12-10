class Retangulo:
    # Atributos
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    # Metodos
    def calcular_area(self):
        return self.altura * self.largura


def main():
    retangulo = Retangulo(int(input('Informe a altura -> ')),
                          int(input('Informe a largura -> ')))

    print(f'A area do retangulo é {retangulo.calcular_area()}')


main()
