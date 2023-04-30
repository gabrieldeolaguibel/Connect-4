# Connect 4
from random import randint


# Create a class implementing stacks using arrays for each column of the game board
class StackUsingArray:  # this is the exact implementation from session 11

    def __init__(self):
        self.stack = []

    def __len__(self):  # define len() method
        return len(self.stack)

    def push(self, element):
        if len(self.stack) >= 0 or len(self.stack) <= 6:  # only push if the column is not full
            self.stack.append(element)
        else:
            return

    def top_element(self):  # return top element of stack without popping it
        return self.stack[-1]


def EmptyGameboard():
    game_rows = []
    for i in range(0, 6): # Fancy way of building game_rows = ["", "", "", "", "", ""]
        game_rows.append([""] * 6)

    lines = []
    for i in range(0, len(game_rows)):
        lines.append([" "] * 7)  # use space later in print function for row borders

    return lines


def game_stacks():
    # apply our stacks to every column in the board
    board_stacks = [StackUsingArray(), StackUsingArray(), StackUsingArray(), StackUsingArray(), StackUsingArray(),
                    StackUsingArray(), StackUsingArray()]
    return board_stacks


# print board
def DisplayGameboard(gameboard):
    board_rows = []
    for i in range(0, 6):  # Fancy way of building game_rows = ["", "", "", "", "", ""]
        board_rows.append([""] * 6)

    bottom_label = "    1   2   3   4   5   6   7   "
    row_struct = [[n] for n in range(0, 7)]
    for i in range(6):
        row_struct[i][0] = "  | "  # build columns lines

    for i in range(0, len(board_rows)):
        for j in range(0, 7):
            row_struct[i][0] = row_struct[i][0] + str(gameboard[i][j]) + " | "  # apply column lines to all rows
        print(row_struct[i][0])
        print("  " + "-" * ((len(row_struct[i][0]) - 3)))  # apply row lines to all columns
    print(bottom_label)
    print(" ")  # add space between boards when they reprint

# function for each of the players movements
def PlayerMove(tile, gameboard, Column_Stacks, bot):
    options = {"1", "2", "3", "4", "5", "6", "7"}
    if tile == bot:
        position = randint(1, 7)  # generate a random play
        if len(Column_Stacks[position - 1]) < 6:  # if the stack is not full
            Column_Stacks[position - 1].push(tile)  # Push the tile to the stack
            # Apply move to gameboard matrix
            gameboard[6 - len(Column_Stacks[position - 1])][position - 1] = Column_Stacks[position - 1].top_element() #position -1 becuase its an array of stacks
        else:
            PlayerMove(tile, gameboard, Column_Stacks, bot)  # try again if stack since stack is full
    else:  # Human Player
        position = str(input("Your turn: "))
        if position not in options:
            print("Invalid input. Please try again")
            PlayerMove(tile, gameboard, Column_Stacks, bot)  # Recursion
        else:
            position = int(position)
            if len(Column_Stacks[position - 1]) < 6:  # if the stack is not full
                Column_Stacks[position - 1].push(tile)  # Push the tile to the stack
                # Apply move to gameboard
                gameboard[6 - len(Column_Stacks[position - 1])][position - 1] = Column_Stacks[position-1].top_element()
            else:
                print("Column is already full, please try again")
                PlayerMove(tile, gameboard, Column_Stacks, bot)  # Recursion
    return gameboard, Column_Stacks


# Check wins
def ScanBoard(tile, gameboard):
    win = False
    # Scan Horizontal
    for i in range(0, 6):
        for j in range(3, 7):  # range to only check 3 spots from the tile
            if gameboard[i][j] == gameboard[i][j - 1] == gameboard[i][j - 2] == gameboard[i][j - 3] == tile: # if they match
                win = True
            else:  # if they don't match
                continue
    # Scan Vertical
    for i in range(0, 7):
        for j in range(3, 6):  # range to only check 3 spots from the tile
            if gameboard[j][i] == gameboard[j - 1][i] == gameboard[j - 2][i] == gameboard[j - 3][i] == tile: # if they match
                win = True
            else:  # if they don't match
                continue
    # Scan Diagonal
    for i in range(0, 4):
        for j in range(0, 3):
            if (gameboard[j][i] == gameboard[j + 1][i + 1] == gameboard[j + 2][i + 2] == gameboard[j + 3][i + 3] == tile  # positive slope
                    or gameboard[j + 3][i] == gameboard[j + 2][i + 1] == gameboard[j + 1][i + 2] == gameboard[j][i + 3] == tile):  # negative slope
                win = True
            else:  # if they don't match
                continue
    if win:
        print(tile + " has won the game!!")
    return win

