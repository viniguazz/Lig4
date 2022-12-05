import Jogador
import random

class Tabuleiro():

    # inicialização
    def __init__(self):
        self.tabuleiro = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

    def getTabuleiro(self):
        return self.tabuleiro
    


    # método que testa a jogada (tanto do humano quanto da IA) e altera o estado do tabuleiro, retornando a) uma lista com a linha e a coluna da jogada, para que o árbitro possa checar o resultado; b) False se a jogada não for viável
    def mudaTabuleiro(self, jogador, humano):
        
        linha = 5
        
        if humano:

            print('Escolha a coluna (digite um número de 1 a 7 e pressione ENTER)!')
            try:
                coluna = int(input('>>> ')) - 1
                while linha >= 0:
                    if self.tabuleiro[linha][coluna] == 0:
                        self.tabuleiro[linha][coluna] = jogador
                        return [True, linha, coluna, jogador]
                    linha = linha - 1 
                return [False]
            except:
                return [False]
        
        else:

            validas = []
            coluna = 0
            while coluna < 7:
                if self.tabuleiro[0][coluna] == 0:
                    validas.append(coluna)
                coluna = coluna + 1
            

            limite = len(validas) - 1
            jogada = random.randint(0, limite)

            linha = 5
            while linha >= 0:
                if self.tabuleiro[linha][jogada] == 0:
                    self.tabuleiro[linha][jogada] = jogador
                    return [True, linha, jogada, jogador]

                linha = linha - 1 


    # método que faz o display do tabuleiro
    def printTabuleiro(self, tabuleiro):
        totalDeLinhas = len(tabuleiro)
        linha = 0

        print()
        print()
        print(45*'\u2500')

        while linha < totalDeLinhas:
            coluna = 0
        
            while coluna < 7:

                if tabuleiro[linha][coluna] == 0:
                    print('\u26AA', end='     ')
                elif tabuleiro[linha][coluna] == 1:
                    print('\U0001F535', end='     ')
                else:
                    print('\U0001F534', end='     ')
            
                coluna = coluna + 1
        
            linha = linha + 1
            print()
            print()
    
        print(45*'\u2500')
        print()