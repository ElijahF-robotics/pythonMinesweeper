# pythonMinesweeper
A basic text-based minesweeper game made with python

It uses mainly the functional programming paradigm and during the building process I was aided 
by GitHub Copilot. 

The game itself includes features such as finding all zeroes adjacent to a zero you hit, and 
the ability to both hit or flag a location

# How to Play
The game is quite simple in its control. It accepts four possible functions:
- hit # #
- flag # #
- superWin
- exit

*NOTE* - For the two functions that accept numbers, the array goes from top to bottom and from left 
to right. Therefore, the top left corner is (1,1), one box right is (2,1), etc.

hit # # is used to hit a specific square. It accepts the column number followed by the row number. 

flag # # is used to flag a specific square. It also accepts the column number followed by the row number

superWin(case sensistive) is used as both a testing function and a cheat code. It solves the whole
board and flags all the mines.

exit is used to end the game
