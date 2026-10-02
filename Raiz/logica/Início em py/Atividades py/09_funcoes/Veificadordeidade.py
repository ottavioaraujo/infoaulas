idade = int(input("qual é sua idade?"))

def verificar_maioridade(idade):
    if idade >= 18:
       return True
    else:
      return False
    

verificar_maioridade(idade)
print(verificar_maioridade(idade))