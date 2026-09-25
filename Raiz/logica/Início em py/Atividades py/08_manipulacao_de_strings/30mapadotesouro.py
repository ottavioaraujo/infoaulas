while True:
 mapa = [
    [" ", " ", " "],  
    [" ", " ", "T"],  
    ["X", " ", " "]  
 ]

 print("--- BEM-VINDO AO CAÇA AO TESOURO ---")
 print("O mapa é uma grade 3x3 (Linhas de 0 a 2 e Colunas de 0 a 2).")

 linha = int(input("Digite a Linha (0 a 2): "))
 coluna = int(input("Digite a Coluna (0 a 2): "))

 if 0 <= linha <= 2 and 0 <= coluna <= 2:
     posicao = mapa[linha][coluna]
     
     if posicao == "T":
         print("Parabéns! Você encontrou o tesouro!")
     elif posicao == "X":
         print("Game Over! Você caiu na armadilha!")
     else:
         print("Apenas terra vazia... Tente novamente.")
 else:
     print("Coordenadas inválidas! Escolha números entre 0 e 2.")

