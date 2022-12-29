# Lig4 / Connect4

(implementation by Vinicius Guazzelli Dias)

This is the OOP discipline's final assignment (1st semester of Computer Information Systems, Federal University of Santa Catarina, taught by Professor Elder Rizzon Santos).
It consists of a Python implementation of the game Lig4 (Connect4), which consists of a 6x7 grid and the objective of the players is to put 4 consecutive gems either verticaly, horizontaly or diagonaly.
The player can choose only in which column it wants to place it's gem, stacking over other placed before.
The paradigm used is OOP.

## Classes

The program has a total of 4 classes: Administrador (administrator), Árbitro (arbiter), Tabuleiro (board) and Jogador (player).


* **Administrador**: greets the player, pics and handles the game mode, collects the player data;

* **Tabuleiro**: displays the board, receives the player's move (or generate the AI's move), checks if the move is licit and, if positive, changes the board;

* **Árbitro**: sets the starting player and checks for a winner;

* **Jogador**: contains the players attributes.

## Main

The Main.py document encases the main logic of the program.



In the near future, I expect to overhaul the interface and implement the minimax algorithm, in order to improve the AI.

Thank you for showing up and checking the (very simple and terribly written) code.

Cheers!
