# Lig4

(implementation by Vinicius Guazzelli Dias)

This is the OOP discipline's final work (1st semester of Computer Information Systems, Federal University of Santa Catarina, taught by Professor Elder).
It consists on a Python implementation of the game Lig4, which consists of a 6x7 grid and the objective of the players is to put 4 consecutive gems either verticaly, horizontaly or diagonaly.
The player can choose only in which column it wants to place it's gem, stacking over other placed before.
The paradigm used is OOP.

## Classes

The program consists of 4 classes: Administrador (Administrator), Arbitro (arbiter), Tabuleiro (Board) and Jogador (player).

### Administrador
Greets the player, pics the game mode, collects the player data.

### Tabuleiro
Displays the board, receives the player's move, checks if the move is licit and, if positive, changes the board.

### Arbitro
Sets the first player, checks for a winner.

### Jogador
Contains the players attributes.

## Main

The Main.py document encases the main logic of the program.
