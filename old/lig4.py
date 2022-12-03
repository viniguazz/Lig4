



tabuleiro = [[0,2,0,2,0,0,1],[0,0,0,0,0,1,2],[0,0,0,0,2,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[1,2,1,1,2,2,1]]


def printTabuleiro(tabuleiro):
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

printTabuleiro(tabuleiro)

input()