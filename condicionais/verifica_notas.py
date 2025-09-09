nota = float(input("Informe a nota -> "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5 and nota <= 6.9:
    print("Em Recuperação")
else:
    print("Reprovado")