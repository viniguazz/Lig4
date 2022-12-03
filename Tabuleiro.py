


class Tabuleiro():

    # inicialização
    def __init__(self):
        self.tabuleiro = [[0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0]]

    def getTabuleiro(self):
        return self.tabuleiro
    


    # método que testa a jogada e altera o estado do tabuleiro, retornando a) uma lista com a linha e a coluna da jogada, para que o árbitro possa checar o resultado; b) False se a jogada não for viável
    def mudaTabuleiro(self, jogador):
        linha = 5
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