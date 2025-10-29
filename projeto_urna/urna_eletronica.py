opcao = -1
senha_encerrar = 1903
encerrar_votacao = 1900
candidatos = []
contagem_votos = {'Nulos': 0}

# Menu principal
while opcao != senha_encerrar:
    opcao = input('O que deseja fazer? \n'
                  'Opção 1: Cadastrar candidato \n'
                  'Opção 2: Iniciar votação \n'
                  'Opção 3: Mostrar votos e vencedor \n'
                  'Opção -> ')

    # Valida se a opção é um numero
    if opcao.isdigit():
        opcao = int(opcao)

        # testa para opções da urna
        if opcao == 1:
            qtd_candidatos = int(input('Quantos candidatos '
                                       'deseja cadastrar -> '))

            # laço para cadastrar candidatos
            for c in range(1, qtd_candidatos+1):
                candidato = []
                nome_candidato = input(f'Nome do candidato {c} -> ')
                num_candidato = int(input(f'Numero do candidato {c} -> '))

                # Salva canditato
                candidato.append(nome_candidato)
                candidato.append(num_candidato)
                # Adiciona candidato na lista principal
                candidatos.append(tuple(candidato))

            print('\n\n')

        elif opcao == 2:
            voto = -1

            while voto != encerrar_votacao:
                # Mostrar lista de candidatos
                for candidato in candidatos:
                    print(f'Candidato {candidato[0]} | Numero {candidato[1]}')

                voto = int(input('Vote no numero de um candidato -> '))

                # Contabilizar a votação
                cont = 0
                for candidato in candidatos:
                    cont += 1
                    if voto == candidato[1]:
                        if candidato[0] not in contagem_votos:
                            contagem_votos.update({candidato[0]: 1})
                            break
                        else:
                            contagem_votos[candidato[0]] += 1
                            break
                    else:
                        if cont == len(candidatos):
                            contagem_votos['Nulos'] += 1

        elif opcao == 3:
            # Remove Nulo incorreto da saida da votação '1900'
            contagem_votos['Nulos'] -= 1

            # Mostra resultados e vencedor
            maior = 0
            vencedor = ''
            for key, value in contagem_votos.items():
                if value > maior:
                    maior = value
                    vencedor = key
                print(f'{key} | Votos {value}')

            print(f'O Vencedor é {vencedor} com {maior} votos')
            print('\n\n')
            # Se a opção digitada não for um numero cai aqui
    else:
        print('\n\nOpção inválida\n\n')
