saldo = 5000
valor_saque = 1

print(f'Seu saldo é {saldo}')

while valor_saque != 0:
    valor_saque = float(input('Informe o valor do saque -> '))
    saldo -= valor_saque
    print(f'Seu saldo é {saldo}')
