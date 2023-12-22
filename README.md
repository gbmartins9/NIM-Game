NIM Game
The NIM game is a classic two-player game where players take turns removing a minimum of 1 and a maximum of M pieces from a table or board containing initially N pieces. The player who removes the last possible pieces wins the game.

There exists a winning strategy for this game that is remarkably simple: it involves always leaving multiples of (M+1) pieces for the opponent.

This Python 3 program allows a user to play NIM against the computer. The computer employs a winning strategy to ensure victory. The logic follows two possible scenarios at the start of the game:

If N is a multiple of (M+1), the computer graciously invites the player to start the game with the phrase "You start!"
Otherwise, the computer takes the initiative to start the game, declaring "Computer starts!"
Once the game begins, the computer's strategy to win involves leaving the player with a number of pieces that are always a multiple of (M+1). If that's not possible, the computer removes the maximum number of pieces allowed.

Enjoy playing against the computer and try to outsmart its strategy!