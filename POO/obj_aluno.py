class Aluno:
    # Atributos
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    # Metodos
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2


def cadastrar_aluno():
    aluno = Aluno(input('Nome do aluno -> '),
                  float(input('Nota 1 do aluno -> ')),
                  float(input('Nota 2 do aluno -> ')))

    return aluno


def main():
    aluno1 = cadastrar_aluno()

    print(f'A media do aluno {aluno1.nome} é {aluno1.calcular_media():.2f}')


main()
