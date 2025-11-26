class SenhaIncorretaError(Exception):
    pass


class SenhaFracaError(Exception):
    pass


def fazer_login(senha_usuario):
    logar = input('\n\nInforme sua senha -> ')

    if logar == senha_usuario:
        print('\nLogin efetuado com sucesso!\n\n')
    else:
        print('\nTente novamente!')
        raise SenhaIncorretaError('Senha incorreta!\n')


def cadastrar_senha():
    print('\nCADASTRO DE SENHA')
    senha_usuario = input('Informe a senha -> ')

    if len(senha_usuario) < 10:
        print('\nTente novamente:')
        raise SenhaFracaError('Senha deve conter 10 caracteres!\n')
    else:
        print('\nSenha cadastrada com sucesso\n')
        return senha_usuario


def menu():
    senha_usuario = '0'
    while True:
        try:
            opcao = int(input(f'1 - Criar senha\n'
                              '2 - Fazer Login \n'
                              '3 - Sair\n'
                              '-> '))
            if opcao == 1:
                senha_usuario = cadastrar_senha()
            elif opcao == 2:
                fazer_login(senha_usuario)
            elif opcao == 3:
                break
            else:
                print('Opção inválida!\n')
                continue
        except SenhaFracaError as erro:
            print(erro)
        except SenhaIncorretaError as erro:
            print(erro)


def main():
    menu()


main()
