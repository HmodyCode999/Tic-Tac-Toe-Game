print("\n\n")
win = 0

# header
import random
import time
def check_winner(board, symbol):
    # تحقق من الصفوف
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # تحقق من الأعمدة
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # تحقق من الأقطار
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

input("Welcome to  Tic-Tac-Toe (X - O) Game   Press  ENTER  for to continue  ")
print("made with love by Hmody     *as usual\n")

# اختيار الشكل
shape = input("Which one U prefer ? \n1. ✖️\n2. ⭕\n-> ")
if shape == "1":
    user_shape = "✖️"
else:
    user_shape = "⭕"
if shape == "1":
    computer_shape = "⭕"
else:
    computer_shape = "✖️"





for row in location :
    print(*row)



while not win :
    ##جزء المستخدم
    # اختيار المستخدم
    choice = int(input("place in -> "))
    
    # ادخال المستخدم
    if choice in check:
        print ("Already Used!!!")
        continue
    elif choice < 4 and choice>0:
        board[0][choice-1] = user_shape
    elif choice < 7 :
        board[1][choice-4] = user_shape
    elif choice < 10 :
        board[2][choice-7] = user_shape
    check.append(choice) 

    # في حاله القائمه اتملت
    if len(check) == 9:
        print("The board is full.")
        play_again = input("Do you want to play again? (yes/no) : ")
        if play_again.lower() == "no":
            break
        else:
            board = main_board
            check.clear()
            continue

    # هل انتصر ؟
    if check_winner(board, user_shape):
        for row in board :
            print(*row)
        print("Player wins!")
        play_again = input("Do you want to play again? (yes/no) : ")
        if play_again.lower() == "no":
            break
        else:
            board = main_board
            check.clear()
            continue
    # عرض اللوحه 
    for row in board :
         print(*row)


    ## جزء الكمبيوتر
    # اختيار الكمبيوتر
    print("\nComputer is making its move...\n")
    time.sleep(1)
    computer_choise = random.randint(1,9)
    while computer_choise in check :
        computer_choise = random.randint(1,9)
        
    # ادخال الكمبيوتر
    if computer_choise < 4 and computer_choise>0:
        board[0][computer_choise-1]=computer_shape
    elif computer_choise < 7 :
        board[1][computer_choise-4]=computer_shape
    elif computer_choise < 10 :
        board[2][computer_choise-7]=computer_shape
    check.append(computer_choise)
    # هل انتصر ؟
    if check_winner(board, computer_shape):
        for row in board :
            print(*row)
        print("Computer wins!")
        play_again = input("Do you want to play again? (yes/no) : ")
        if play_again.lower() == "no":
            break
        else:
            board = main_board
            check.clear()
            continue

    # عرض اللوحه 
    for row in board :
         print(*row)

print("\n\n")



#?       Follow us  ฅ⁠^⁠•⁠ﻌ⁠•⁠^⁠ฅ
#!    Youtube ->   @ZU Informatics
#*     GitHub  ->  @HmodyCode999