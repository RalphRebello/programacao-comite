tupla = (1, 2, 3, 4, 5, 6, 3, 2, 1, 5, 6, 7, 8, 9)

numeros_unicos = []

for i in tupla:
    if i not in numeros_unicos:
        numeros_unicos.append(i)

tupla_final = tuple(numeros_unicos)

print(*tupla_final)
print(type(tupla_final))
