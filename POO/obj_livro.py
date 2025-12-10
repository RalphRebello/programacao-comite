class Livro:
    # Atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    # Metodos
    def exibir_info(self):
        print(f'Titulo: {self.titulo}')
        print(f'Autor: {self.autor}')


def main():
    titulo = input('Informe o titulo do livro -> ')
    autor = int(input('Informe a autor do livro -> '))
    livro1 = Livro(titulo, autor)
    livro1.exibir_info()


main()
