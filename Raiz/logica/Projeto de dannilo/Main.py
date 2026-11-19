# randomizar escolhas
import random
#para time sleep
import time
# importando a biblioteca questionary para usar as setas para escolher opções no terminal
import questionary


print("\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██▀▀▀▀\033[0;94;44m▓▒░\033[0;34m█\033[0;37m \033[0;94m▀███\033[0;94;44m▒░ \033[0;34m▀\033[0;37m \033[0;94m▀\033[0;94;44m▒░░\033[0;34m██▀\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m▄▄\033[0;37m  \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██▀▀▀▀\033[0;94;44m▓▒░\033[0;34m█\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m▄▄\033[0;37m        \033[0;94m▀███\033[0;94;44m▒░ \033[0;34m▀▀▀\033[0;94;44m▒░░\033[0;34m█▄\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m▄▄\033[0;37m   \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██▀\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒\033[0;34m█▄▄\033[0m")
print("\033[0;37m \033[0;94;44m▓▒░\033[0;34m███\033[0;37m    \033[0;94;44m▒░░\033[0;34m█\033[0;37m  \033[0;94;44m█▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m██\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m    \033[0;94;44m▒░░\033[0;34m█\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m██\033[0;37m        \033[0;94;44m█▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m███\033[0;37m   \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓░\033[0;34m███\033[0m")
print("\033[0;37m \033[0;94;44m▒░\033[0;34m████\033[0;37m     \033[0;34m▀▀▀\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m  \033[0;94;44m▒░\033[0;34m████\033[0;37m     \033[0;34m▀▀▀\033[0;37m  \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m        \033[0;94;44m▓▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m  \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m          \033[0;34m▀\033[0;94;44m░\033[0;34m████▄▄▄\033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████▄▄\033[0;94;44m░\033[0;34m███▀\033[0;37m   \033[0;94;44m░\033[0;34m█████▄▄▄█▄\033[0;37m     \033[0;94;44m░\033[0;34m█████▄▄\033[0;94;44m░\033[0;34m███▀\033[0;37m         \033[0;94;44m▒░\033[0;34m████\033[0;37m \033[0;34m▄▄▄▄▄▄▄\033[0;37m  \033[0;94;44m░\033[0;34m█████▄▄\033[0;94;44m░\033[0;34m███▀\033[0;37m    \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m                   \033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m█▄\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;34m▀\033[0;37m      \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m███▄\033[0;37m        \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m███▄\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▓▒░\033[0;34m█\033[0;37m  \033[0;34m██\033[0;94;44m░▒\033[0;34m█\033[0;37m    \033[0;94;44m▒░\033[0;34m███\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▓▒░\033[0;34m█\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m        \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▒░\033[0;34m██\033[0;37m  \033[0;34m▀████▄\033[0;37m \033[0;34m▄\033[0;94;44m░\033[0;34m████▀\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m \033[0;34m▄\033[0;94;44m░\033[0;34m████▀\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▒░\033[0;34m██\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m        \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m \033[0;34m▄\033[0;94;44m░\033[0;34m████▀\033[0m")
print("\033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m     \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m     \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m    \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀\033[0;37m        \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m   \033[0m")


# falta desenvolver
def iniciar_jogo(nome=None):
    
    time.sleep(1)

    nome = input("Qual é seu nome?")

    if not nome:
        return

    nome, vida, Exp, energia = variaveis_universais(nome)

    jogador = {
        "nome": nome,
        "vida": vida,
        "Exp": Exp,
        "energia": energia,
        "inventario": []
    }

    print(f"\nseu nome é: {nome}\n\nvida: {vida}\nExperiencia: {Exp} \nenergia: {energia}\n")

    menu_no_jogo(jogador)


def explorar(jogador):
    print("explorando...")
    time.sleep(1)

    itens = ["Firewall Portátil", "Patch de Correção", "Chave de Acesso"]

    item_sorteado = random.choice(itens)
    jogador["inventario"].append(item_sorteado)

    print(f"Voce encontrou um {item_sorteado}!")

    jogador["Exp"] += 10
    jogador["energia"] -= 10

    menu_no_jogo(jogador)


# definição das variaveis universais por meio de uma função
def variaveis_universais(nome):
    # nome do user
    # vida do user
    vida = 100
    # experiencia do user
    Exp = 67
    # energia do user
    energia = 50

    return nome, vida, Exp, energia


# cabecalho de boas vindas
print("SEJA BEM VINDO AO CYBER GRID!! \n \n ")


# Cria a lista de opções
opcoes = [
    "Iniciar novo jogo",
    "ver instrucoes",
    "Sair"
]


# implementar questionary para selecionar as opcoes do menu
def menu_no_jogo(jogador):

    while True:
        print("1-Continuar\n2-Inventario\n3-Explorar\n4-Sair")

        opcoes_m = [
            "Continuar",
            "Inventario",
            "Explorar",
            "Sair"
        ]

        escolha = questionary.select(
            "Use as setas para escolher uma opção e aperte Enter:",
            choices=opcoes_m
        ).ask()

        if escolha is None or escolha == "Sair":
            return

        elif escolha == "Continuar":
            mostrar_status(jogador)

        elif escolha == "Inventario":
            inventario(jogador)

        elif escolha == "Explorar":
            jogador["energia"] -= 0
            explorar(jogador)


def inventario(jogador):
    print("\nSeus itens são:")

    if jogador["inventario"]:
        for item in jogador["inventario"]:
            print(f"- {item}")
    else:
        print("Seu inventário está vazio.")

    return


def mostrar_status(jogador):
    print(f"\nseu nome é: {jogador['nome']}")
    print(f"vida: {jogador['vida']}")
    print(f"Experiencia: {jogador['Exp']}")
    print(f"energia: {jogador['energia']}\n")


def game_over():
    print("O jogo terminou")
    print("Obrigado por jogar")

    ques = questionary.select(
        "Quer jogar novamente?",
        choices=["sim", "nao"]
    ).ask()

    if ques == "sim":
        return iniciar_jogo()
    else:
        return menu_do_jogo()


# falta desenvolver
def ver_instruncoes():
    print('intruções...')
    questionary.press_any_key_to_continue().ask()


# selecao com setas
def menu_do_jogo():

    while True:

        # Cria a lista de opções
        opcoes = [
            "Iniciar novo jogo",
            "ver instrucoes",
            "Sair"
        ]

        # Exibe o menu e aguarda a escolha do usuário
        escolha = questionary.select(
            "Use as setas para escolher uma opção e aperte Enter:",
            choices=opcoes
        ).ask()

        if escolha is None:
            break

        # mostra as instrucoes do jogo
        if escolha == "ver instrucoes":
            ver_instruncoes()

        # inicia o jogo
        elif escolha == "Iniciar novo jogo":
         print("\nIniciando jogo", end="", flush=True)
         for _ in range(3):
          time.sleep(0.4)
          print(".", end="", flush=True)   
          print()
         iniciar_jogo()

        # sai do jogo com animacao dos pontos
        elif escolha == "Sair":
                    print("Encerrando Cyber Grid", end="", flush=True)
                    for _ in range(3):
                        time.sleep(0.4)
                        print(".", end="", flush=True)
                        
                    
                    break
        


menu_do_jogo()