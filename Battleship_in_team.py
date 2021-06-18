
import os
import random
import sys
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

def user_board_size(): #CLAUDIU
    correct_choice = False
    while correct_choice != True:
        print(""" Please chose board size :
                    1 - 5 x 5
                    2 - 10 x 10
                    3 - You can choose board size (from 6 to 9)
                    """)
        user_choice = input("Your choice is :")
        if user_choice in ["1","2","3"]:
            correct_choice = True
            if user_choice == "1":
                user_board_size = 7
            elif user_choice == "2":
                user_board_size = 12
            elif user_choice == "3":
                user_board_size = set_user_board_size()+2
        else :
            print("Something went wrong, try again")
    return user_board_size

def set_user_board_size(): #CLAUDIU
    correct_choice = False
    while correct_choice != True:
        board_size = int(input("What size do you choose? (from 6 to 9) :"))
        if board_size in [6,7,8,9]:
            correct_choice = True
            return board_size
        else :
            print("Something went wrong, try again")
            
def limit_turn(): #ANDREI  #de aratat dupa fiecare miscare pentru jucatori cate mutari disponibile mai are 
    correct_choice = False
    while correct_choice != True:
        turn = input("Please select how many moves do you want! Between 5 and 50: ")
        if turn.isnumeric():
            turn = int(turn)
        else:
            print(""" ERROR 404: NOT FOUND! """)
            continue
        if turn in range(5, 51):
            correct_choice = True
            return turn * 2
        else:
            print(""" ERROR 404: NOT FOUND! """)

def check_fit (board_size, ship_size, user_row, user_column, ship_orientation): #TOATA ECHIPA
        if ship_orientation == (1, 0):
            if user_column + ship_size <= board_size - 1:
                return True
            else :
                print("Ship will not fit in the table(H)")
                return False
        if ship_orientation == (-1, 0):
            if user_column + ship_size <= board_size - 1:
                return True
            else :
                print("Ship will not fit in the table(H)")
                return False
        if ship_orientation == (0, 1):
            if user_row + ship_size <= board_size -1:
                return True
            else :
                print("Ship will not fit in the table(V)")
                return False
        if ship_orientation == (0, -1):
            if user_row + ship_size <= board_size - 1:
                return True
            else :
                print("Ship will not fit in the table(V)")
                return False               

def check_correct_positon (board, ship_size, user_row, user_column, ship_orientation): #TOATA ECHIPA            
    for row in range(user_row - 1, user_row + 2):        
        for column in range (user_column -1, user_column + ship_size + 1):
            try :
                if row < 0 or column < 0:
                    pass
                else :
                    if board[row][column] == "0":
                        pass
                    else:
                        return False
                        break
            except IndexError:
                continue
    return True

def init_board(board_size): #DRAGOS
    board = []
    for i in range(board_size):
        board.append(["0"]*(board_size))    
    return board
    
def show_board(board, board_size): #ROBERT
    print("  ",end ="")
    for number in range (1,board_size-1):
        print(number,end=" ")
    for row in range(1,board_size-1):
        ascii_letter = 64 + row
        print()
        print(chr(ascii_letter),end = " ")
        for column in range(1,board_size-1):
            print(board[row][column], end=" ")
    print()

def get_ship_orientation() : #DRAGOS
    print(""" Choose ship orientation :
                N
                S
                E
                W       
            """)
    ship_orientation = input("Your choice is (N, S, E, W):").upper()
    if ship_orientation == "N":
        return (0, 1)
    elif ship_orientation == "S":
        return (0, -1)
    elif ship_orientation == "E":
        return (1, 0)
    elif ship_orientation == "W":
        return (-1, 0)
    else:
        print("Something went wrong, try again")
        get_ship_orientation()

def get_ship_coridnates(): #ANDREI
    print("""Chose ship`s position (first field).
            Row - (from A to E)
            Column (from 1 to 5))
            """)
    user_row, user_column = get_coordinates(board_size)
    return user_row,user_column

def get_shot_coridnates(board_displayed): #MIHAI
    correct_choice = False
    while correct_choice != True:
        print("""Chose shot position. (first field).
                Row - (from A to E)
                Column (from 1 to 5)
                """)
        user_row, user_column = get_coordinates(board_size)
        if board_displayed[user_row][user_column] == "0":
            correct_choice = True
        else:
            print("You have already given this coordinate. Try again")
    return user_row,user_column

def get_coordinates(board_size): #DRAGOS
    letter_5x5 = ("a","b","c","d","e")
    letter_6x6 = ("a","b","c","d","e",'f')
    letter_7x7 = ("a","b","c","d","e",'f','g')
    letter_8x8 = ("a","b","c","d","e",'f','g','h')
    letter_9x9 = ("a","b","c","d","e",'f','g','h','i')
    letter_10x10 = ("a","b","c","d","e","f","g","h","i","j") 
    correct_choice = False
    while correct_choice != True:
        user_row_letter = input("Enter the row first :")
        if board_size == 7:
            if user_row_letter.lower() not in letter_5x5:
                print("Not an appropriate choice")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_choice = True
        elif board_size == 8:
            if user_row_letter.lower() not in letter_6x6:
                print("Not an appropriate choice")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_choice = True
        elif board_size == 9:
            if user_row_letter.lower() not in letter_7x7:
                print("Not an appropriate choice")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_choice = True
        elif board_size == 10:
            if user_row_letter.lower() not in letter_8x8:
                print("Not an appropriate choice")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_choice = True
        elif board_size == 11:
            if user_row_letter.lower() not in letter_9x9:
                print("Not an appropriate choice")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_choice = True
        elif board_size == 12:
            if user_row_letter.lower() not in letter_10x10:
                print("Not an appropriate choice")
            else:
                user_row = int(ord(user_row_letter.lower())- 96)
                correct_choice = True
        else:
            user_row = int(ord(user_row_letter.lower())- 96)
            correct_choice = True
    correct_choice = False
    while correct_choice != True:
        try:
            user_column = int(input("Enter the column now :"))
            if board_size == 7:
                if user_column > 5:
                    print("Not an appropriate choice")
                else :
                    correct_choice = True
            else: correct_choice = True
            if board_size == 8:
                if user_column > 6:
                    print("Not an appropriate choice")
                else :
                    correct_choice = True
            else: correct_choice = True
            if board_size == 9:
                if user_column > 7:
                    print("Not an appropriate choice")
                else :
                    correct_choice = True
            else: correct_choice = True
            if board_size == 10:
                if user_column > 8:
                    print("Not an appropriate choice")
                else :
                    correct_choice = True
            else: correct_choice = True
            if board_size == 11:
                if user_column > 9:
                    print("Not an appropriate choice")
                else :
                    correct_choice = True
            else: correct_choice = True
            if board_size == 12:
                if user_column > 10:
                    print("Not an appropriate choice")
                else :
                    correct_choice = True
        except ValueError:
            print("Something went wrong.Please try again")
    return user_row, user_column

def random_shot_coordinates(board_size,board_displayed): #CLAUDIU
    correct_choice = False
    while correct_choice != True:
        random_row = random.randint(1,board_size - 2)
        random_column = random.randint(1,board_size - 2)
        if board_displayed[random_row][random_column] == "0":
            correct_choice = True
        else :    
            pass
    return random_row, random_column
    
def take_value_field(board,row,column): #####
    return board[row][column]

def mark_ships(board, ship_size, ship_orientation, user_row, user_column): #MIHAI
    if ship_orientation == (1, 0):
        for column in range(user_column, user_column + ship_size):
            board[user_row][column] = "X"
    elif ship_orientation == (-1, 0):
        for column in range(user_column, user_column + ship_size):
            board[user_row][column] = "X"
    elif ship_orientation == (0, 1):
        for row in range(user_row, user_row + ship_size):
            board[row][user_column] = "X"
    elif ship_orientation == (0, -1):
        for row in range(user_row, user_row + ship_size):
            board[row][user_column] = "X"
            
def mark_board(board,row,column,sign): #####
    board[row][column] = sign

def set_ships(ship_list,board):  #ANDREI  
    for ship in range (len(ship_list)):
        completed_ship = False
        os.system("cls || clear")
        show_board(board, board_size)
        while completed_ship == False:            
            print (f'Set position for the ship of size: {ship_list[ship]} \n')
            ship_size = ship_list[ship]        
            ship_orientation = get_ship_orientation()
            user_row, user_column = get_ship_coridnates()
            if check_correct_positon(board, ship_size, user_row, user_column, ship_orientation) is True and check_fit(board_size,ship_size,user_row,user_column,ship_orientation):
                mark_ships(board, ship_size, ship_orientation, user_row, user_column)
                completed_ship = True
                os.system("cls || clear")
            else:
                print("You cant put ship here. Try again")                
        show_board(board, board_size)  

def random_set_ships(ship_list,board): #CLAUDIU
    for ship in ship_list:
        completed_ship = False
        while completed_ship == False:
            ship_size = ship
            ship_orientation, user_row, user_column = random_ship_coordinates(board_size)
            if check_correct_positon(board, ship_size, user_row, user_column, ship_orientation) is True and check_fit(board_size,ship_size,user_row,user_column,ship_orientation):
                mark_ships(board, ship_size, ship_orientation, user_row, user_column)
                completed_ship = True
            else:
                pass

def two_boards (board_1,board_2): #DRAGOS
    print("  ",end ="")
    for number in range (1,len(board_1)-1):
        print(number,end=" ")
    if len(board_1) > 9:
        print("     ",end="")
    else:
        print("      ",end="")
    for number in range (1,len(board_2)-1):
        print(number,end=" ")

    for row in range(1,len(board_1)-1):
        ascii_letter = 64 + row
        print()
        print(chr(ascii_letter),end = " ")
        for column in range(1,len(board_1)-1):
            print(board_1[row][column], end=" ")
        print("    ",end="")
        print(chr(ascii_letter),end = " ")
        for column in range(1,len(board_2)-1):
            print(board_2[row][column], end=" ")
    print()

def random_ship_coordinates(board_size): #CLAUDIU
    ship_orientation = random.randint(1,2)
    if ship_orientation == 1:
        ship_orientation = (1, 0) or (-1, 0)
    else :
        ship_orientation = (0, 1) or (0, -1)
    random_row = random.randint(1,board_size - 1)
    random_column = random.randint(1,board_size - 1)
    return ship_orientation, random_row, random_column

def give_a_shot(player,sequence): #MIHAI
    if player == "player_2" and 'player_1':
        board = board_1
        board_displayed = board_1_displayed
    else:
        board = board_2
        board_displayed = board_2_displayed
    next_shot = True
    while next_shot == True:
        print(f"Now {player}")
        if game_mode == "1":
            user_shot_row, user_shot_column = get_shot_coridnates(board_displayed)
        elif game_mode == "2" and sequence % 2 == 0:
            user_shot_row, user_shot_column = get_shot_coridnates(board_displayed)
        else :            
            user_shot_row, user_shot_column = random_shot_coordinates(board_size,board_displayed)
        user_shot_value = take_value_field(board,user_shot_row,user_shot_column)
        print(f'You chose {user_shot_row} {user_shot_column}')
        if user_shot_value == "0":
            board_displayed[user_shot_row][user_shot_column] = "M"
            os.system("cls || clear")
            print("You've missed!")            
            next_shot = False
        elif user_shot_value == "X":
            mark_board(board_displayed,user_shot_row,user_shot_column,"H")
            ship_elements.clear()
            check_adjacent(board,user_shot_row,user_shot_column, "X")
            if is_sunk(board_displayed) is True:
                os.system("cls || clear")
                print("You've sunk a ship!\n")
                mark_ship_sunk(board_displayed)
            else:
                os.system("cls || clear")
                print("You've hit a ship!\n")
        win = has_won(board_displayed, player)
        if win == True:
            quit(player)
        two_boards(board_1_displayed, board_2_displayed)

def has_won(board, player): #CLAUDIU
    count_s_element = 0    
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == "S":
                count_s_element += 1
    if len(board) == 7:
        if count_s_element == 3: 
            return sys.exit(f"{player} has won the game!")
        else:   
            return False
    if len(board) == 12:
        if count_s_element == 6:
            return sys.exit(f"{player} has won the game!")
    if len(board) == 8:
        if count_s_element == 3:
            return sys.exit(f"{player} has won the game!")
    if len(board) == 9:
        if count_s_element == 3:
            return sys.exit(f"{player} has won the game!")
    if len(board) == 10:
        if count_s_element == 6:
            return sys.exit(f"{player} has won the game!")
    if len(board) == 11:
        if count_s_element == 6:
            return sys.exit(f"{player} has won the game!")
        else:   
            return False
   

def check_adjacent(board, row, column, sign): ######
    if board[row+1][column] == sign and check_ship_elements(row+1,column) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row+1, column, sign)
    elif board[row+1][column] == sign and check_ship_elements(row+1,column) == True:
        pass

    if board[row-1][column] == sign and check_ship_elements(row-1,column) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row-1, column, sign)
    elif board[row-1][column] == sign and check_ship_elements(row-1,column) == True:
        pass   
    
    if board[row][column+1] == sign and check_ship_elements(row,column+1) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row, column+1, sign)
    elif board[row][column+1] == sign and check_ship_elements(row,column+1) == True:
        pass

    if board[row][column-1] == sign and check_ship_elements(row,column-1) == False:
        ship_elements.append([row,column])
        check_adjacent(board,row, column -1, sign)
    elif board[row][column-1] == sign and check_ship_elements(row,column-1) == True:
        pass  
    if board[row][column] == sign and check_ship_elements(row,column) == False:
        ship_elements.append([row,column])
            
    if board[row][column] == "0" or board[row][column] =="M":
        if len(ship_elements) == 1:
            pass
        else:
            check_adjacent(board,ship_elements[0][0],ship_elements[0][1],sign)
    
def check_ship_elements(row,column): ####
    for element in ship_elements:
        if element == [row,column]:
            return True
    return False

def is_sunk(board_displayed): #MIHAI   
    for element in ship_elements:
        row = element[0]
        column = element[1]
        if board_displayed[row][column] != "H":
            return False
    return True

def mark_ship_sunk(board_displayed): #MIHAI
    for element in ship_elements:
        row = element[0]
        column = element[1]
        board_displayed[row][column] = "S"

def is_tie(turn): #CLAUDIU
    if turn == 0:
        sys.exit("It's a tie!")
    else:
        return False

def choose_random_filling(): #CLAUDIU
    correct_choice = False
    if correct_choice != True:
        print("""Do you want to randomly fill the board.
                Y - Yes
                N - No""")
        random_filling = input('Choose "y" or "n": ').lower()
        if random_filling == "y":
            correct_choice = True
            return True
        elif random_filling == "n":
            correct_choice = True
            return False
        else:
            print("Something went wrong.Please try again")

def fill_empty_boards(game_mode): #CLAUDIU
    if game_mode == "1":
        if choose_random_filling() is True:
            random_set_ships(ship_list, board_1)
        else :
            set_ships(ship_list, board_1)
        print("You have finished positioning the ships")
        os.system("cls || clear")
        input("Press ENTER to allow the next player to position the ships")
        if choose_random_filling() is True:
            random_set_ships(ship_list, board_2)
        else :
            set_ships(ship_list, board_2)
        print("You have finished positioning the ships")
        os.system("cls || clear")
    else :
        if choose_random_filling() is True:
            random_set_ships(ship_list, board_1)
        else :
            set_ships(ship_list, board_1)
        print("You have finished positioning the ships")
        os.system("cls || clear")
        input("Press ENTER to allow the computer to position the ships")
        random_set_ships(ship_list, board_2)
   
def game_mode(): #TOATA ECHIPA
    correct_choice = False
    while correct_choice != True:
        print("""Please chose game mode :
                    1 - Player vs Player
                    2 - Player vs Computer
                    3 - Ai vs AI (XXX)
                    """)        
        game_mode = input("Your choice is :")
        if game_mode in ["1","2","3"]:
            correct_choice = True
            return game_mode
        else:
            print("Something went wrong, try again")

ship_elements = []

def get_number_of_ship(board_size):
    if board_size <= 7:
        ship_list = [1, 2]
    elif board_size >= 7:
        ship_list = [1, 2, 3]
    return ship_list


def play_game():    
    two_boards(board_1_displayed, board_2_displayed)
    sequence = 0
    global turn
    for sequence in range(turn):
        if sequence % 2 == 0:
            give_a_shot('player_1',sequence)
            turn -= 1
            print(f"Turns left:{turn//2}")         
        else:    
            give_a_shot('player_2',sequence)
            turn -= 1
            print(f"Turns left:{turn//2}")
        if turn == 0:
            is_tie(turn)
  

game_mode = game_mode()
board_size = user_board_size()
turn = limit_turn()
ship_list = get_number_of_ship(board_size)
board_1 = init_board(board_size)
board_2 = init_board(board_size)
board_1_displayed = init_board(board_size)
board_2_displayed = init_board(board_size) 
fill_empty_boards(game_mode)

if __name__ == '__main__':
    play_game()