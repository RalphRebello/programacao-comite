lado_1 = int(input("Informe o valor do primeiro lado "))
lado_2 = int(input("Informe o valor do segundo lado "))
lado_3 = int(input("Informe o valor do terceiro lado "))

if lado_1 + lado_2 > lado_3 or \
   lado_2 + lado_3 > lado_1 or \
   lado_1 + lado_3 > lado_2:
    print("Triango válido!")

    if lado_1 == lado_2 == lado_3:
        print("Triangulo equilatero")
    elif lado_1 == lado_2 or \
            lado_2 == lado_3 or \
            lado_1 == lado_3:
        print("Triangulo Isóceles")
    elif lado_1 != lado_2 != lado_3:
        print("Triangulo escaleno")
    else:
        print("Outro tipo")
else:
    print("Triangulo inválido")
