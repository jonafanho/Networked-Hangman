# Networked Hangman
A networked hangman game by John Kim and Jonathan Ho.

Start server.py to initiate networked hangman.

Each player needs to start client.py to play game.

First player to join the server will become the host of first game and decide on the word for other players to guess

Anyone is allowed to guess at any time (no turns)

Each guess must be a letter, no complete word. 

When a guess is longer than a letter, the server will take the first letter as a guess

Repeated guess will not be counted as an attempt

The game is over when there is no more unknown letters of the word or 8 missed attempts

When game is over, the order the players are connected decide the next game host.

