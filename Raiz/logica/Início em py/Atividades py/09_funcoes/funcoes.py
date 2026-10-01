print("CALCULADORA")
print("SOMA = 1, SUBTRAÇÃO = 2, MULTIPLICAÇÃO = 3, DIVISÃO = 4, POTENCIAÇÃO = 5")
escolha = input("Digite uma operação: ")

n1 = float(input("Digite um número para a sua operação: "))
n2 = float(input("Digite outro número para a sua operação: "))


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def potenciar(a, b):
    # Se o expoente for inteiro, calcular usando loop for
    if b == int(b):
        exp = int(b)
        if exp < 0:
            # expoente negativo: calcular potência e depois inverter
            result = 1
            for _ in range(abs(exp)):
                result *= a
            if result == 0:
                return "Erro: divisão por zero na potenciação"
            return 1 / result
        else:
            result = 1
            for _ in range(exp):
                result *= a
            return result
    # Caso contrário, usa operador ** para expoentes não inteiros
    return a ** b


def operacoes(numero1, numero2, opcao):
    match opcao:
        case '1':
            return somar(numero1, numero2)
        case '2':
            return subtrair(numero1, numero2)
        case '3':
            return multiplicar(numero1, numero2)
        case '4':
            return dividir(numero1, numero2)
        case '5':
            return potenciar(numero1, numero2)
        case _:
            return "Operação inválida"


resultado = operacoes(n1, n2, escolha)
print(f"Resultado: {resultado}")
