import random

lista = []
pares = []

for i in range(10):
    lista.append(random.randint(1, 100))

for i in lista:
    if i % 2 == 0:
        pares.append(i)

print('Lista original:', *lista)
print('Lista de numeros pares:', *pares)
