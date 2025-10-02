import random

n = random.randint(1, 100)
chute = 0
tentativas = 0

while True:
    chute = int(input('Chute um numero -> '))
    tentativas += 1

    if chute == n:
        print(f'PARABÉNS VOCÊ ACERTOU COM {tentativas} TENTATIVAS!!!')
        break
    elif chute < n:
        print(f'O numero {chute} é menor que o numero secreto')
    elif chute > n:
        print(f'O numero {chute} é maior que o numero secreto')
