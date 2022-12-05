import os
import Administrador
import Tabuleiro
import Arbitro
from time import sleep

sair = False

while not sair:

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
            licito = tabuleiro.mudaTabuleiro(jogador1.numero, jogador1.humano)
            while not licito[0]:
                print('Jogada inválida! Tente novamente.')
                licito = tabuleiro.mudaTabuleiro(jogador1.numero, jogador1.humano)
            jogada = jogada + 1
            turno = 2

        else:
            os.system('cls')
            print()
            print()
            print(f'############## Jogador 2 - {jogador2.nome} #################')
            tabuleiro.printTabuleiro(tabuleiro.tabuleiro)
            licito = tabuleiro.mudaTabuleiro(jogador2.numero, jogador2.humano)
            while not licito[0]:
                print('Jogada inválida! Tente novamente.')
                licito = tabuleiro.mudaTabuleiro(jogador2.numero, jogador2.humano)
            jogada = jogada + 1
            turno = 1
        
        print(f'jogada numero {jogada}')
        sleep(0.5)

        vencedor = arbitro.verificarVencedor([licito[1], licito[2], licito[3]], tabuleiro.tabuleiro)

        if vencedor:
            os.system('cls')
            tabuleiro.printTabuleiro(tabuleiro.tabuleiro)

    if licito[3] == 1:
        print(f'Parabéns {jogador1.nome}! Você venceu!')
    else: 
        print(f'Parabéns {jogador2.nome}! Você venceu!')

    continuar = input('Jogar novamente? Digite 1 e pressione ENTER. Digite qualquer outra tecla e pressione ENTER para sair.\n>>>')
    if continuar != '1':
        sair = True