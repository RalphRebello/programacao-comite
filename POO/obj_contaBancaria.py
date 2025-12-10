class Conta:
    # Atributos
    def __init__(self, saldo):
        self.saldo = int(saldo)

    # Metodos
    def depositar(self, valor):
        print(f'\nSaldo anterior | {self.saldo} |')
        self.saldo += valor
        print(f'Saldo atual | {self.saldo} |')

    def sacar(self, valor):
        print(f'\nSaldo anterior | {self.saldo} |')
        self.saldo -= valor
        print(f'Saldo atual | {self.saldo} |')


def main():
    minha_conta = Conta(3000)
    minha_conta.sacar(int(input('Informe valor do saque -> ')))

    print(f'\nO saldo atual é {minha_conta.saldo}\n')

    minha_conta.depositar(int(input('Informe valor do deposito -> ')))


main()
