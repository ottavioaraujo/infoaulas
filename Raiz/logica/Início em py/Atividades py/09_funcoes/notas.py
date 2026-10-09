def cadastrar_aluno(nome, nota1, nota2):
    media_calculada = (nota1 + nota2) / 2
    return {"nome": nome, "media": media_calculada}


def verificar_situacao(media, media_corte=6.0):
    if media >= media_corte:
        return "Aprovado"
    return "Reprovado"
    
def exibir_relatorio(lista_alunos):
    if not lista_alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- RELATÓRIO DE NOTAS DO LABORATÓRIO ---")
    print(f"{'Nome':<20} | {'Média':<6} | {'Situação':<10}")
    print("-" * 43)

    for aluno in lista_alunos:
        nome = aluno["nome"]
        media = aluno["media"]
        situacao = verificar_situacao(media)

        print(f"{nome:<20} | {media:<6.1f} | {situacao:<10}")


def iniciar():
    alunos = []

    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Verificar situação")
        print("3 - Exibir relatório")
        print("4 - Sair")
        escolha = int(input("\nEscolha: "))

        if escolha == 1:
            nome = input("Nome do aluno: ")
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            alunos.append(cadastrar_aluno(nome, nota1, nota2))
            print("Aluno cadastrado com sucesso!")

        elif escolha == 2:
            if not alunos:
                print("Nenhum aluno cadastrado.")
                continue

            nome = input("Digite o nome do aluno: ")
            aluno_encontrado = None

            for aluno in alunos:
                if aluno["nome"].lower() == nome.lower():
                    aluno_encontrado = aluno
                    break

            if aluno_encontrado is None:
                print("Aluno não encontrado.")
            else:
                print(
                    f"{aluno_encontrado['nome']} está {verificar_situacao(aluno_encontrado['media'])}."
                )

        elif escolha == 3:
            exibir_relatorio(alunos)

        elif escolha == 4:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


iniciar()
