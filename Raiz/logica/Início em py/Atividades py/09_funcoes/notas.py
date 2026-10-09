def cadastrar_aluno(nome, nota1, nota2):

    media_calculada = (nota1 + nota2) / 2
    
   
    return {"nome": nome, "media": media_calculada}


def verificar_situacao(media, media_corte=6.0):
    if media >= media_corte:
        return "Aprovado"
    else:
        return "Reprovado"


def exibir_relatorio(lista_alunos):
    print("\n--- RELATÓRIO DE NOTAS DO LABORATÓRIO ---")
    print(f"{'Nome':<20} | {'Média':<6} | {'Situação':<10}")
    print("-" * 43)
    
    for aluno in lista_alunos:
        nome = aluno["nome"]
        media = aluno["media"]
       
        situacao = verificar_situacao(media)
        
        print(f"{nome:<20} | {media:<6.1f} | {situacao:<10}")
