from random import randint
import Tabuleiro

class Arbitro():

    def __init__(self):
        pass

    # sorteira o primeiro jogador
    def sorteio(self):
        num = randint(1,10)
        if num <= 5:
            return 1
        else:
            return 2

    
    # verifica se há algum jogador vencedor após a jogada
    def verificarVencedor(self, jogada, tabuleiro):
        linha = jogada[0]
        coluna = jogada[1]
        jogador = jogada[2]
        indice = 0

        #verificação horizontal
        while indice < 7:
            if tabuleiro[linha][indice] == jogador:
                horizontal = horizontal + 1
            else:
                horizontal = 0
            indice = indice + 1

        indice = 0

        #verificação vertical
        while indice < 6:
            if tabuleiro[indice][coluna] == jogador:
                vertical = vertical + 1
            else:
                vertical = 0
            indice = indice + 1
        
        indice = 0

        # verificação da diagonal esquerda
        i = linha
        j = coluna
        diagEsquerda = 0
        while i >= 0 or j >= 0:
            i = i - 1
            j = j + 1

        while i <= 6 or j <= 7:
            if tabuleiro[i][j] == jogador:
                diagEsquerda = diagEsquerda + 1
            else:
                diagEsquerda = 0
            i = i + 1
            j = j - 1

        # verificação da diagonal direita
        i = linha
        j = coluna
        diagDireita = 0
        
        while i >= 0 or j >= 0:
            i = i - 1
            j = j - 1

        while i <= 6 or j <= 7:
            if tabuleiro[i][j] == jogador:
                diagEsq = diagEsq + 1
            else:
                diagDireita = 0
            i = i + 1
            j = j + 1
   
        if horizontal >= 0 or vertical >= 4 or diagEsq >= 4 or diagDireita >= 4:
            return True
        
        return False



