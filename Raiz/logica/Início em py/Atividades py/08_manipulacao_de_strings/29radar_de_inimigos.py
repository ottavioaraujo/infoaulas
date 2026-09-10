
radar = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]

contador = 0

for linha in radar:
    for valor in linha:
        if valor == 1:
            contador += 1

print(radar)
print(f"Inimigos: {contador}")
