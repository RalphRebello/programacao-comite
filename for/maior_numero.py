maior = 0

for numero in range(0, 5):
    valor = int(input(f'Informe o {numero + 1}º numero -> '))

    if valor > maior:
        maior = valor

print(f'O maior numero foi {maior}')
