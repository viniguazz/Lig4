'''
    def intro(self):
        selecao = False
        os.system('cls')
        while not selecao:
            print()
            print()
            print('##############    LIG 4    ##############')
            print()
            print()
            print('Implementado por Vinicius Guazzelli Dias')
            print()
            print()
            print('Escolha o modo de jogo:')
            print('\u2600 1 Jogador')
            print('  2 Jogadores')
            print()
            print()
            entrada = int(input())
            print('a entrada foi ', entrada)
            if entrada == 2:
                selecao = True
                print('foi')
                os.system('cls')
                print()
                print()
                print('##############    LIG 4    ##############')
                print()
                print()
                print('Implementado por Vinicius Guazzelli Dias')
                print()
                print()
                print('Escolha o modo de jogo:')
                print('1 Jogador')
                print('\u2600 2 Jogadores')
                print()
                print()
'''
        
'''
            def setPosicaoTabuleiro(self, linha, coluna, valor):
        self.tabuleiro[linha][coluna-1] = valor

        '''