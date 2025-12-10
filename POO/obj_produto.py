class Produto:
    # Atributos
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    # Metodos
    def aplicar_desconto(self, desconto):
        return self.valor - self.valor * desconto / 100


def cadastrar_produto():
    p = Produto(input('Nome do produto -> '),
                float(input('Valor do produto -> ')))

    return p


def main():
    p1 = cadastrar_produto()
    p_desconto = p1.aplicar_desconto(
        int(input('Informe o percetual de desconto -> ')))

    print(f'Preço normal do produto {p1.nome} | R${p1.valor:.2f}')
    print(f'Preço com desconto do produto {p1.nome} | R${p_desconto:.2f}')


main()
