numeros = []
for i in range(5):
    numeros.append(int(input(f'Informe o {i+1}º numero -> ')))

print(f'Os números digitados foram ', end=' ')
for i in numeros:
    print(i, end=' ')
print(f'\nO maior número digitado foi {max(numeros)}')
print(f'O menor número digitado foi {min(numeros)}')
print(f'O média dos números é {sum(numeros)/len(numeros)}')
