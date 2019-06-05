# Networked Hangman
A networked Hangman game by [John Kim](https://github.com/kimj41) and [Jonathan Ho](https://github.com/jonafanho).

## Installation
Download and extract or clone this repository. The server must be started before the clients. Clients are the actual players; an unlimited number of clients can be opened. Both the server and client can be started with the command line.

### Starting the Server
```python server.py [serverPort]```
### Starting the Client
```python client.py [serverName] [serverPort]```
### Arguments
```serverName``` An optional argument to specify the server ip.

```serverPort``` An optional argument to specify the port to use.

## Gameplay
If you are unfamilar with Hangman, [please read the rules before continuing](https://www.wikihow.com/Play-Hangman).

1. The first player to join the server will be the game master. This player can decide the word for other players to guess.
    * Only one word can be entered.
    * If the word contains a space, only the section before the space will be used.
    * The ```/random``` command can be used. See below.

2. When the game starts, all players can enter letters (no turns).
    * The game master can enter letters in case there is a need to give hints.
    * Each guess must be a letter, not a complete word.
    * If a guess is longer than a letter, only the first letter will be used.

3. The game is over when all the letters have been guessed or if there are eight incorrect guesses.
    * Repeated guesses of the same letter will be ignored.
    * Scores will be awarded.
      * If all the letters have been guess, all players except for the game master will earn one (1) point.
      * If there are eight incorrect guesses, the game master will earn one (1) point.
      * Scores are saved until the server closes or when players disconnect.

4. When the game is over, the next player who joined the game will be selected as next game host.

## Commands
```/random```
  * When the game master is choosing a word, the ```/random``` command can be used to generate a random word from a list of the 3000 most popular English words.

```/say <message>```
  * When the game has begun, the ```/say``` command broadcasts a message to all players.
  * Players can ask for hints, chat, or send funny jokes.
  * Arguments
    * ```<message>``` The message to send. Required.

## Notes
Tested with the Windows Command Prompt on Windows 10.
