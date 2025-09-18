soma_impares = 0

for numero in range(1, 101):
    if numero % 2 != 0:
        # soma_impares = soma_impares + numero
        soma_impares += numero
        print(soma_impares)
