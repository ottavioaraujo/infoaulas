with open("Raiz/logica/Início em py/Atividades py/11_manipulucao_de_arquivos/notas.txt", "w", encoding="utf-8") as arquivo:
    for nomes in range(1,3):

        nome = input("Digite o nome do aluno\n")
        nota = input("Digite a nota do aluno\n") 

        arquivo.write(f"NOME | {nome}\nNOTA | {nota}\n \n")