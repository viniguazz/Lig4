import os
import Administrador
import Tabuleiro
import Jogador
import Arbitro
from time import sleep

tabuleiro = Tabuleiro.Tabuleiro()
adm = Administrador.Administrador()
arbitro = Arbitro.Arbitro()


jogador1, jogador2 = adm.iniciarJogo(adm.intro())
turno = arbitro.sorteio()

jogada = 0

vencedor = False

while not vencedor and jogada != 42:

    if turno == 1:
        os.system('cls')
        print()
        print()
        print(f'############## Jogador 1 - {jogador1.nome} #################')
        tabuleiro.printTabuleiro(tabuleiro.tabuleiro)
        licito = tabuleiro.mudaTabuleiro(jogador1.numero)
        while not licito[0]:
            print('Jogada inválida! Tente novamente.')
            licito = tabuleiro.mudaTabuleiro(jogador1.numero)
        jogada = jogada + 1
        turno = 2

    else:
        os.system('cls')
        print()
        print()
        print(f'############## Jogador 2 - {jogador2.nome} #################')
        tabuleiro.printTabuleiro(tabuleiro.tabuleiro)
        licito = tabuleiro.mudaTabuleiro(jogador2.numero)
        while not licito[0]:
            print('Jogada inválida! Tente novamente.')
            licito = tabuleiro.mudaTabuleiro(jogador2.numero)
        jogada = jogada + 1
        turno = 1
    
    print(f'jogada numero {jogada}')
    sleep(1)

    #vencedor = arbitro.verificarVencedor([licito[1], licito[2], licito[3]], tabuleiro.tabuleiro)

print('cabô')