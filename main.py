from game_functions import *

# Main program
def main():
    print("Welcome to Connect 4!")

    # Player chooses game piece
    selection = str(input("Choose your game piece (X or O): "))
    if selection != "X" and selection != "O" and selection != "x" and selection != "o":  # not case sensitive
        selection = str(input("invalid selection. Please choose again (X or O): "))
    if selection == "X" or selection == "x":
        bot = "O"
    else:
        bot = "X"

    # Print gameboard
    gameboard = EmptyGameboard()  # call the function with the lines of the board
    Stacks = game_stacks()  # call the function with the stacksa of each column
    DisplayGameboard(gameboard)  # print it

    print("Instructions: Enter the column you would like to drop your tile in.")
    print("The first player to connect 4 tiles (vertically, diagonally, or horizontally) wins!")
    win = False
    while not win:
        # X player
        gameboard, Stacks = PlayerMove('X', gameboard, Stacks, bot)  # call the function to allow player move
        DisplayGameboard(gameboard)  # show the board with the chosen move
        win = ScanBoard('X', gameboard)  # check for a win
        if win:
            break
        # O player
        board, Stacks = PlayerMove('O', gameboard, Stacks, bot)  # call the function to allow player move
        DisplayGameboard(gameboard)  # show the board with the chosen move
        win = ScanBoard('O', gameboard)  # check for a win
        if win:
            break
    print("Thanks for playing!")


if __name__ == '__main__':
    main()

