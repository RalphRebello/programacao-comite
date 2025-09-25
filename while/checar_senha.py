senha = ''

while senha != 'comite':
    senha = input('Digite a senha -> ')

##############################################

while True:
    if senha == 'comite':
        print('Acesso liberado!')
        break
    else:
        senha = input('Informe a senha -> ')
