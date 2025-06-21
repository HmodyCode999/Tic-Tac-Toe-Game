print("\n\n")
win = 0

# header
import random
import time
def check_winner(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False
main_board = [
     ["⬜", "⬜", "⬜"],
     ["⬜", "⬜", "⬜"],
     ["⬜", "⬜", "⬜"]
]
board = [
     ["⬜", "⬜", "⬜"],
     ["⬜", "⬜", "⬜"],
     ["⬜", "⬜", "⬜"]
]
location = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]
check = []
user_shape = ""
computer_shape = ""

input("Welcome to Tic-Tac-Toe (X - O) Game   Press ENTER to continue  ")
print("made with love by Hmody     *as usual\n")

# Shape selection
shape = input("Which one do you prefer? \n1. ✖️\n2. ⭕\n-> ")
if shape == "1":
    user_shape = "✖️"
else:
    user_shape = "⭕"
if shape == "1":
    computer_shape = "⭕"
else:
    computer_shape = "✖️"

for row in location:
    print(*row)

while not win:
    ## Player's turn
    # Player's choice
    choice = int(input("place in -> "))
    
    # Player's input
    if choice in check:
        print("Already Used!!!")
        continue
    elif choice < 4 and choice > 0:
        board[0][choice-1] = user_shape
    elif choice < 7:
        board[1][choice-4] = user_shape
    elif choice < 10:
        board[2][choice-7] = user_shape
    check.append(choice)

    # Check if board is full
    if len(check) == 9:
        print("The board is full.")
        play_again = input("Do you want to play again? (yes/no) : ")
        if play_again.lower() == "no":
            break
        else:
            board = main_board
            check.clear()
            continue

    # Check for player win
    if check_winner(board, user_shape):
        for row in board:
            print(*row)
        print("Player wins!")
        play_again = input("Do you want to play again? (yes/no) : ")
        if play_again.lower() == "no":
            break
        else:
            board = main_board
            check.clear()
            continue
    # Display board
    for row in board:
         print(*row)

    ## Computer's turn
    # Computer's choice
    print("\nComputer is making its move...\n")
    time.sleep(1)
    computer_choice = random.randint(1,9)
    while computer_choice in check:
        computer_choice = random.randint(1,9)
        
    # Computer's input
    if computer_choice < 4 and computer_choice > 0:
        board[0][computer_choice-1] = computer_shape
    elif computer_choice < 7:
        board[1][computer_choice-4] = computer_shape
    elif computer_choice < 10:
        board[2][computer_choice-7] = computer_shape
    check.append(computer_choice)
    # Check for computer win
    if check_winner(board, computer_shape):
        for row in board:
            print(*row)
        print("Computer wins!")
        play_again = input("Do you want to play again? (yes/no) : ")
        if play_again.lower() == "no":
            break
        else:
            board = main_board
            check.clear()
            continue

    # Display board
    for row in board:
         print(*row)

print("\n\n")

# Follow me  ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ
# GitHub  -> @HmodyCode999
