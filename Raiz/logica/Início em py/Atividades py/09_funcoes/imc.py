peso = int(input("qual é seu peso?"))
altura = float(input("qual é sua altura?"))

def calcular(peso,altura):
    imc = peso/altura**2
    print(f"seu imc é {imc:.2f}")
    if imc < 18.5:
        print("voceesta abaixo do peso")
    elif imc > 18.5 or imc < 24.9:
        print("peso ideal parabens")
    elif imc > 25 or imc < 29.9:
            print("Voce esta um poco acima do peso,cuidado")
    elif imc > 30.0  or imc < 34.9:
            print("obesidade I")
    elif imc > 35.0  or imc < 39.9:
                print("obesidade II (severa)")
    elif imc > 40.0:
        print("obesidade III (morbida)")
        
    return imc

calcular(peso,altura)