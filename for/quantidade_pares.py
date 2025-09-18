quantidade_pares = 0
for numero in range(2, 51, 2):
    quantidade_pares += 1

print(quantidade_pares)

# ###############################################

for indice, numero in enumerate(range(2, 51, 2)):
    print(indice + 1, numero)
