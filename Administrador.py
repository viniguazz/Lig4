import os
import Jogador
from time import sleep


class Administrador():

    def __init__(self):
        self.turno = 0
    

    # método que exibe a tela inicial e retorna a opção de jogo eleita pelo jogador (ou a opção de saída do programa)
    @staticmethod
    def intro():

        os.system('cls')        
        print()
        print()
        print('##############    LIG 4    ##############')
        print('Implementado por Vinicius Guazzelli Dias')
        print()
        print()


        entrada = ''
        while entrada != 1 and entrada != 2 and entrada != 0:
            print('Escolha o modo de jogo:')
            print()
            print('1 Jogador -> Digite 1 e aperte ENTER')
            print('2 Jogadores -> Digite 2 e aperte ENTER')
            print('Sair -> Digite 0 e aperte ENTER')
            print()
            
            naoInteiro = True
            while naoInteiro:
                try:
                    entrada = int(input('>>> '))
                    naoInteiro = False
                    print('entrada: ', entrada)
                except:
                    os.system('cls')
                    print('====Entrada inválida!====')
                    print('1 Jogador -> Digite 1 e aperte ENTER')
                    print('2 Jogadores -> Digite 2 e aperte ENTER')
                    naoInteiro = True
            os.system('cls')
            print('====Entrada inválida!====')
        return entrada


    # método que administra a opção de modo de jogo eleito pelo player
    def iniciarJogo(self, modo):
        if modo == 0:
            print('Arregou, que feio! Até a próxima!')
            quit()

        elif modo == 1:
            os.system('cls')
            print()
            print('1 JOGADOR')
            print()
            print('Digite o seu nome: ')
            nome = input('>>> ')
            jogador1 = Jogador.Jogador(nome, 1, True)
            jogador2 = Jogador.Jogador('Máquina', 2, False)
            os.system('cls')
            print()
            print()
            print(f' ####### {jogador1.nome} vs {jogador2.nome}!!! Preparem-se! ####### ')
            sleep(3)
            return(jogador1, jogador2)
            

        else:
            os.system('cls')
            print()
            print('2 JOGADORES')
            print()
            print('Digite o seu nome (jogador 1): ')
            nome = input('### ')
            jogador1 = Jogador.Jogador(nome, 1, True)
            print('Digite o seu nome (jogador 2): ')
            nome = input('>>> ')
            jogador2 = Jogador.Jogador(nome, 2, False)
            os.system('cls')
            print()
            print()
            print(f' ####### {jogador1.nome} vs {jogador2.nome}!!! Preparem-se! ####### ')
            sleep(3)
            return(jogador1, jogador2)





    
