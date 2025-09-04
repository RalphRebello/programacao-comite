# Antecessor e sucessor
numero_1 = int(input("Informe um numero -> "))
print("Antecessor -> ", numero_1 - 1,
      "Sucessor -> ", numero_1 + 1)

# Conversor de °C -> °F
temperatura_c = float(input("Informe a temperatura °C -> "))
temperatura_f = (temperatura_c * 9 / 5) + 32
print("Temperatura em °F -> ", temperatura_f)

# quociente inteiro e resto da divisão
numero_1 = int(input("Informe o primeiro numero -> "))
numero_2 = int(input("Informe o segundo numero -> "))
print("Quociente inteiro -> ", numero_1 // numero_2, "\n", 
      "Resto da divisão -> ", numero_1 % numero_2)

# Calcular a potencia
base = int(input("Informe o valor da base -> "))
expoente = int(input("Informe o valor do expoente -> "))
print("O resultado da potencia é -> ", base ** expoente)