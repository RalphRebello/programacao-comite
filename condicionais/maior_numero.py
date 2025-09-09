numero_1 = int(input("Informe o primeiro numero -> "))
numero_2 = int(input("Informe o segundo numero -> "))
numero_3 = int(input("Informe o terceiro numero -> "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("O numero", numero_1, "é o maior!")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("O numero", numero_2, "é o maior!")
elif numero_1 == numero_2 == numero_3:
    print("Os numero são iguais")
else:
    print("O numero", numero_3, "é o maior!")