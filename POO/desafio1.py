# ==========================
#  SISTEMA DE BIBLIOTECA
# ==========================

# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __repr__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} ({self.autor}) - {status}"


# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Usuário: {self.nome}"


# Classe Biblioteca
class Biblioteca:
    def __init__(self, livros):
        self.livros = livros

    def emprestar(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"📚 {usuario.nome} emprestou '{livro.titulo}'.")
                    return
                else:
                    print(f"❌ O livro '{livro.titulo}' já está emprestado.")
                    return
        print(f"⚠️ Livro '{titulo}' não encontrado no acervo.")

    def devolver(self, titulo, usuario):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"✔️ {usuario.nome} devolveu '{livro.titulo}'.")
                    return
                else:
                    print(f"❌ O livro '{livro.titulo}' já estava disponível.")
                    return
        print(f"⚠️ Livro '{titulo}' não existe na biblioteca.")

    def listar_livros(self):
        print("\n📘 LISTA DE LIVROS:")
        for livro in self.livros:
            print("•", livro)
        print()


# ==========================
#  SIMULAÇÃO DO SISTEMA
# ==========================

def main():
    # Criando usuários
    u1 = Usuario("Ana")
    u2 = Usuario("Bruno")
    u3 = Usuario("Carla")

    # Criando livros
    l1 = Livro("O Hobbit", "J.R.R. Tolkien")
    l2 = Livro("Dom Casmurro", "Machado de Assis")
    l3 = Livro("1984", "George Orwell")
    l4 = Livro("A Revolução dos Bichos", "George Orwell")
    l5 = Livro("A Arte da Guerra", "Sun Tzu")

    # Criando biblioteca
    biblioteca = Biblioteca([l1, l2, l3, l4, l5])

    # Listando livros antes
    biblioteca.listar_livros()

    # Empréstimos
    biblioteca.emprestar("1984", u1)
    biblioteca.emprestar("O Hobbit", u2)
    biblioteca.emprestar("1984", u3)  # tentando retirar novamente

    # Devoluções
    biblioteca.devolver("1984", u1)
    biblioteca.emprestar("1984", u3)  # agora funciona

    # Listando ao final
    biblioteca.listar_livros()
main()