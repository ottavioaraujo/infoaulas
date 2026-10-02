celsius = float(input("Qual temperatura deseja converter?"))

def conversor(celsius):
    fahrenheit = (celsius * 1.8 + 32)
    print(f"a conversao de {celsius}cº para fh é {fahrenheit}")
            
    return fahrenheit

conversor(celsius)
          