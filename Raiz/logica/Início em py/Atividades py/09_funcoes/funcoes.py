print("CALCULADORA")
opcoes = ("SOMA = 1 , SUBTRAÇAO = 2  MULTIPLICAÇAO = 3 , DIVISAO = 4  POTENCCIAÇAO = 5")
print(opcoes)
escolha = (input("digite uma operacao"))

n1 = ("digite um numero para a sua operacao")
n2 = ("digite outro numero para a sua operacao")

def operacoes (soma,subtracao,multi,divisao,potencia):
    soma = (n1 + n2)
    subtracao = (n1 - n2)
    multi = (n1*n2)
    divisao = (n1/n2)
    potencia = (n1**n2)

    return soma,subtracao,multi,divisao,potencia

match escolha:
    case '1' :
        soma
    case  '2' :
        subtracao
    case  '3' :
        multi
    case  4 :
        divisao
    case  5 :
        potencia
