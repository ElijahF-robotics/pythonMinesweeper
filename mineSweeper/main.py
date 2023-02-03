# This is a text-based minesweeper game
import random
from os import system, name
from tabulate import tabulate
import time


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def printArray(array):
    print(tabulate(array, tablefmt="rounded_grid"))


# The following function accepts an array and a list of coordinates
def updateArray(array, x, givenArray=None, startValue="*"):
    if givenArray is not None:
        array[x[1] - 1][x[0] - 1] = givenArray[x[1] - 1][x[0] - 1]
    else:
        array[int(x[1]) - 1][x[0] - 1] = startValue


def createGrid(x=10, y=10, startValue="*"):
    return [[startValue for i in range(y)] for j in range(x)]


def randomizeMines(array, mines):
    for i in range(mines):
        x = random.randint(0, len(array) - 1)
        y = random.randint(0, len(array[0]) - 1)
        array[x][y] = "M"


def surroundGrid(n1, n2):  # Accepts coordinates of an object, returns array of possible locations
    array = [
        [n1 - 1, n2 - 1],
        [n1 - 1, n2],
        [n1 - 1, n2 + 1],

        [n1, n2 - 1],
        [n1, n2 + 1],

        [n1 + 1, n2 - 1],
        [n1 + 1, n2],
        [n1 + 1, n2 + 1]
    ]
    return array


def findNumbers(numArray, mineArray):
    for i in range(len(numArray)):
        for j in range(len(numArray[i])):
            temp = surroundGrid(i, j)
            for k in temp:
                if k[0] >= 0 and k[1] >= 0:
                    try:
                        if mineArray[k[0]][k[1]] == "M":
                            numArray[i][j] += 1
                    except IndexError:
                        pass


def revealTouchingZeroes(numBoard, x, y, mineBoard):
    rows, cols = len(numBoard), len(numBoard[0])
    possible = surroundGrid(x, y)
    revealed = []

    def reveal(r, c):
        print("reveal r and c: ", r, c)
        if r < rows and c < cols and [r, c] not in revealed and mineBoard[r][c] != "M":
            if numBoard[r][c] == 0:
                revealed.append([r, c])
                possible.extend(surroundGrid(r, c))
    try:
        for i in possible:
            reveal(i[0], i[1])

    except IndexError:
        pass

    return revealed


def main():
    X_SIZE = 10
    Y_SIZE = 8

    visualArray = createGrid(X_SIZE, Y_SIZE) # This is the array that the user sees

    mineArray = createGrid(X_SIZE, Y_SIZE,)  # This is the array that tracks the mines
    randomizeMines(mineArray, 10)

    numbersArray = createGrid(X_SIZE, Y_SIZE, 0)  # This is the array that contains the numbers
    findNumbers(numbersArray, mineArray)

    printArray(visualArray)

    rand = [random.randint(0, X_SIZE - 1), random.randint(0, Y_SIZE - 1)]

    # Pick a start value to help along
    while mineArray[rand[0]][rand[1]] != "M":
        rand = [random.randint(0, X_SIZE - 1), random.randint(0, Y_SIZE - 1)]

    updateArray(visualArray, rand, numbersArray)
    clear()
    printArray(visualArray)

    amountOfMines = 10
    amountOfFlags = 0
    amountRevealed = 0

    while True:
        x = input("Enter command: ")
        x = x.split(" ")
        command = x.pop(0)
        x = [int(i) for i in x]

        if command == "exit":
            break

        elif command == "flag":
            updateArray(visualArray, x, startValue=">")
            clear()
            printArray(visualArray)
            amountOfFlags += 1
            continue

        elif command == "superWin":
            for i in range(len(visualArray)):
                for j in range(len(visualArray[i])):
                    if mineArray[i][j] != "M":
                        updateArray(visualArray, [j + 1, i + 1], numbersArray)
                    elif mineArray[i][j] == "M":
                        updateArray(visualArray, [j + 1, i + 1], startValue=">")
            clear()
            amountRevealed = (X_SIZE * Y_SIZE) - amountOfMines
            amountOfFlags = amountOfMines
            printArray(visualArray)

        elif command == "hit":
            if numbersArray[x[1] - 1][x[0] - 1] == 0:
                print("You hit a zero!")
                zeroes = revealTouchingZeroes(numbersArray, x[1] - 1, x[0] - 1, mineArray)
                time.sleep(1)
                for i in zeroes:
                    updateArray(visualArray, [i[1] + 1, i[0] + 1], numbersArray)
                clear()
                printArray(visualArray)

            elif mineArray[x[1] - 1][x[0] - 1] == "M":
                print("You hit a mine!")
                break

            else:
                updateArray(visualArray, x, numbersArray)
                clear()
                printArray(visualArray)

            amountRevealed += 1

        if amountRevealed == (X_SIZE * Y_SIZE) - amountOfMines:
            print("You win!")
            break

if __name__ == "__main__":
    main()