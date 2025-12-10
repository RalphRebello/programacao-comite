class Pessoa:
    # Atributos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Metodos
    def apresentar(self):
        print(f'Olá, seja bem vindo {self.nome}')
        print(f'Você está com {self.idade} anos')


def main():
    nome = input('Informe o nome da pessoa -> ')
    idade = int(input('Informe a idade da pessoa -> '))
    pessoa1 = Pessoa(nome, idade)
    pessoa1.apresentar()


main()
