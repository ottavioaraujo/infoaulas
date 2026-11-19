#importando a biblioteca questionary para uar a setas para escoher opcoes no terminal
import random
import time

import questionary

print("\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██▀▀▀▀\033[0;94;44m▓▒░\033[0;34m█\033[0;37m \033[0;94m▀███\033[0;94;44m▒░ \033[0;34m▀\033[0;37m \033[0;94m▀\033[0;94;44m▒░░\033[0;34m██▀\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m▄▄\033[0;37m  \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██▀▀▀▀\033[0;94;44m▓▒░\033[0;34m█\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m▄▄\033[0;37m        \033[0;94m▀███\033[0;94;44m▒░ \033[0;34m▀▀▀\033[0;94;44m▒░░\033[0;34m█▄\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m▄▄\033[0;37m   \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██▀\033[0;37m \033[0;94m▀\033[0;94;44m█▓▒░\033[0;34m██\033[0;94m▀\033[0;94;44m█▓▒\033[0;34m█▄▄\033[0;37m \033[0m")
print("\033[0;37m \033[0;94;44m▓▒░\033[0;34m███\033[0;37m    \033[0;94;44m▒░░\033[0;34m█\033[0;37m  \033[0;94;44m█▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m██\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m    \033[0;94;44m▒░░\033[0;34m█\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m██\033[0;37m        \033[0;94;44m█▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m██\033[0;37m   \033[0;94;44m▓▒░\033[0;34m███\033[0;37m   \033[0;94;44m▓▒░\033[0;34m███\033[0;37m  \033[0;94m▀\033[0;94;44m▓░\033[0;34m███\033[0m")
print("\033[0;37m \033[0;94;44m▒░\033[0;34m████\033[0;37m     \033[0;34m▀▀▀\033[0;37m  \033[0;94;44m▓▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m  \033[0;94;44m▒░\033[0;34m████\033[0;37m     \033[0;34m▀▀▀\033[0;37m  \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m        \033[0;94;44m▓▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m  \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m   \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▒░\033[0;34m████\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m          \033[0;34m▀\033[0;94;44m░\033[0;34m████▄▄▄\033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████▄▄\033[0;94;44m░\033[0;34m███▀\033[0;37m   \033[0;94;44m░\033[0;34m█████▄▄▄█▄\033[0;37m     \033[0;94;44m░\033[0;34m█████▄▄\033[0;94;44m░\033[0;34m███▀\033[0;37m         \033[0;94;44m▒░\033[0;34m████\033[0;37m \033[0;34m▄▄▄▄▄▄▄\033[0;37m  \033[0;94;44m░\033[0;34m█████▄▄\033[0;94;44m░\033[0;34m███▀\033[0;37m    \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m                   \033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m  \033[0;94m▀\033[0;94;44m▓▒░\033[0;34m█▄\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;34m▀\033[0;37m      \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m███▄\033[0;37m        \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m███▄\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▓▒░\033[0;34m██\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▓▒░\033[0;34m█\033[0;37m  \033[0;34m██\033[0;94;44m░▒\033[0;34m█\033[0;37m    \033[0;94;44m▒░\033[0;34m███\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▓▒░\033[0;34m█\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m        \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m▒░\033[0;34m███\033[0m")
print("\033[0;37m \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▒░\033[0;34m██\033[0;37m  \033[0;34m▀████▄\033[0;37m \033[0;34m▄\033[0;94;44m░\033[0;34m████▀\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m \033[0;34m▄\033[0;94;44m░\033[0;34m████▀\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m    \033[0;94;44m▒░\033[0;34m██\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m        \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m  \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m   \033[0;94;44m░\033[0;34m█████\033[0;37m \033[0;34m▄\033[0;94;44m░\033[0;34m████▀\033[0m")
print("\033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m     \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m     \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m    \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀\033[0;37m        \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀\033[0;37m \033[0;34m▀▀▀▀▀▀▀▀▀▀▀▀\033[0;37m   \033[0m")

#falta desenvonvolver
def iniciar_jogo(nome):
    print("iniciano jogo...")
    time.sleep(1)
    # variavel que pede o nome do user
    nome = input("Qual é seu nome?")
    #chamar variaveis da funcao
    nome,vida,Exp,energia = variaveis_universais(nome)
    # mostrar stats
    print(f"\nseu nome é:{nome}\n\nvida:{vida}\nExperiencia:{Exp} \nenergia:{energia}\n")
    menu_no_jogo()
    return nome

def explorar():
    print("explorando...")
    time.sleep(1) 
    achar_itens = random.randint(1,10)

    itens = ["Firewall Portátil","Patch de Correção","Chave de Acesso", ]
    item_sorteado = random.choice(itens)
    inventario.append(item_sorteado)
    print(f"Voce encontrou um {item_sorteado}!")
   
    menu_no_jogo()

# definição das variaveis universais por meio e uma função
def variaveis_universais(nome):
    #nome do user
    nome
    #vida do user
    vida = 100
    #experiencia do user
    Exp = 67
    #energia do user
    energia = 50

    return nome,vida,Exp,energia


# cabecalho de boa vindas
print("SEJA BEM VINDDO AO CYBER GRID!! \n \n ")



# Cria a lista de opções
opcoes = [
    "Iniciar novo jogo",
    "ver instrucoes",
    "Sair"
]

#implementar questionary para selecionar as opcoes do menu
def menu_no_jogo():
    print("1-Continuar\n2-Inventario\n3-Explorar\n4-Sair")
    escolha = input("Selecione:")
    match escolha:
        case "1":
            print("\nContinuando o jogo...\n")
        case "2":
            inventario()
        case "3":
            menu_do_jogo()
            exit(0)
        case "4":
            print("Saindo do jogo...")
            exit(0)
        case _:
            print("escolha 1,2 ou 3")


def inventario():
    inventario = []
    print(f"Seus intens sao: {inventario}")
    return menu_no_jogo()

      
def game_over():
     print("O jogo terminou")
     print(" obrigado por jogar")
     ques = input("quer jogar novamente? sim/nao:")
     match ques:
        case "sim":
                 return iniciar_jogo()
        case "nao":
              return menu_do_jogo()
        case _:     
                exit(0)

#falta desenvonvolver
def ver_instruncoes():
    print('intruções...')

# selecao com setas
def menu_do_jogo():
    # Cria a lista de opções
    opcoes = [
        "Iniciar novo jogo",
        "ver instrucoes",
        "Sair"
    ]

    # Exibe o menu e aguarda a escolha do usuário
    escoha = questionary.select(
        "Use as setas para escolher uma opção e aperte Enter:",
        choices=opcoes
    ).ask()

    # Mostra o que o usuario escolheu
    print(f"\nVocê selecionou: {escoha}")
    # mostra as instrucoes do jogo
    if escoha == "ver instrucoes":
        ver_instruncoes()
    # inicia o jogo
    elif escoha == "Iniciar novo jogo":
        iniciar_jogo(nome)
    # sai do jogo
    elif escoha == "Sair":
        print("Encerrando o programa...")
        exit(0)

    elif escoha == "Sair":
        print("Encerrando o programa...")
        exit(0)
escolha = questionary.select(
    "Use as setas para escolher uma opção e aperte Enter:",
    choices=opcoes
).ask()

# Mostra o que o usuario escolheu
print(f"\nVocê selecionou: {escolha}")

if escolha == "ver instrucoes":
    ver_instruncoes()

elif escolha == "Iniciar novo jogo":
    iniciar_jogo(None)


elif escolha == "Sair":
    print("Encerrando o programa...")
    exit(0)



