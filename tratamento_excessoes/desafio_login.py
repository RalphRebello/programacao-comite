class UsuarioNaoEncontrado(Exception):
    pass


class SenhaInvalida(Exception):
    pass


# Banco de usuários fictício (poderia ser um dicionário, BD etc.)
usuarios = {
    "ralph": "12345",
    "admin": "admin123",
    "user": "senha"
}


def validar_login(usuario, senha):
    if usuario not in usuarios:
        raise UsuarioNaoEncontrado("Usuário não encontrado!")

    if usuarios[usuario] != senha:
        raise SenhaInvalida("Senha incorreta!")

    return True


def sistema_login():
    tentativas = 0
    limite = 3

    while tentativas < limite:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        try:
            if validar_login(usuario, senha):
                print("\nLogin realizado com sucesso!\n")
                return

        except UsuarioNaoEncontrado as erro:
            print(f"Erro: {erro}")
        except SenhaInvalida as erro:
            print(f"Erro: {erro}")

        tentativas += 1
        print(f"Tentativas restantes: {limite - tentativas}\n")

    print("\nLimite de tentativas atingido. Tente novamente mais tarde.\n")


def main():
    sistema_login()


main()
