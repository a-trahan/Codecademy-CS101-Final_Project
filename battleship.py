# I will try to keep things organized
# imports (if any)
import random
# dictionaries
index_to_letter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
letter_to_index = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
# global scope variables (if any)
play = True
# max board width is 26, typical 10
board_width = 10
# no fixed max height, typical 10
board_height = 10
# starting board; typical ships/spaces: Carrier 5, Battleship 4, Destroyer 3, Submarine 3, Patrol Boat 2; [row, col, desc]; fixed list for now
player_board = [[0,0,"Carrier"],[0,1,"Carrier"],[0,2,"Carrier"],[0,3,"Carrier"],[0,4,"Carrier"],[4,1,"Destroyer"],[2,1,"Destroyer"],[3,1,"Destroyer"],[9,4,"Battleship"],[9,5,"Battleship"],[9,6,"Battleship"],[9,7,"Battleship"],[4,7,"Submarine"],[5,7,"Submarine"],[6,7,"Submarine"],[8,2,"Patrol Boat"],[8,3,"Patrol Boat"]]
opponent_board = [[4,1,"Carrier"],[4,2,"Carrier"],[4,3,"Carrier"],[4,4,"Carrier"],[4,4,"Carrier"],[7,0,"Destroyer"],[8,0,"Destroyer"],[9,0,"Destroyer"],[1,3,"Battleship"],[2,3,"Battleship"],[3,3,"Battleship"],[4,3,"Battleship"],[3,8,"Submarine"],[4,8,"Submarine"],[5,8,"Submarine"],[7,5,"Patrol Boat"],[8,5,"Patrol Boat"]]
# [row, col, desc]; x-hit o-miss
player_shots = []
player_score = 0
opponent_shots = []
opponent_score = 0
# functions (if any)


def prep_board(board):
    display_board = []
    #blank board
    for row in range(board_height):
        display_board.append([])
        for col in range(board_width):
            display_board[row].append("[ ]")
    for ship in board:
        display_board[ship[0]][ship[1]] = str(ship[2])[:3]
    return display_board

def display_game_board(board):
    string_to_print = "   "
    for col in range(board_width):
        string_to_print += " {letter} ".format(letter = index_to_letter[col+1].upper())
    for row in range(board_height):
        string_to_print += "\n" + str(row+1) + " " *max(3-len(str(row+1)),0)

        for col in range(board_width):
            string_to_print += board[row][col]
    return string_to_print

def main_menu():
    print("Available options: 1-view player board, 2-see past shots, 3-take a shot, 8-help, 0-quit game")
    menu_input = input("Type option here: ")
    if menu_input == "1":
        print(display_game_board(prep_board(player_board)))
        main_menu()
    elif menu_input == "2":
        print(display_game_board(prep_board(player_shots)))
        main_menu()
    elif menu_input == "3":
        player_shot()
        if player_score >= 17:
            print("Player has won!")
        elif opponent_score >= 17:
            print("Opponent has won!")
        else:
            print("Current score {player_score}:player, {opponent_score}:opponent".format(player_score=player_score, opponent_score=opponent_score))
            main_menu()
    elif menu_input == "8":
        help_menu()
        main_menu()
    elif menu_input =="0":
        print("Thanks for playing!")
    elif menu_input == "cheat":
        print(display_game_board(prep_board(opponent_board)))
        main_menu()
    else:
        main_menu()

def player_shot():
    cell = input("Which cell? (eg. \"A2\" no quotes) ").strip()
    did_hit = ""
    marker = ""
    cell_row = int(cell[1:])-1
    cell_col = int(letter_to_index[cell[0].lower()])-1
    if cell_row+1 > board_height or cell_col+1 > board_width:
        print("Invalid cell, try again.")
        return
    for shot in player_shots:
        if shot[0] == cell_row and shot[1] == cell_col:
            retry = input("You've made that shot before. 1-retry, 2-continue").strip()
            if retry == "1":
                main_menu()
            else:
                pass
    check_opponent = prep_board(opponent_board)
    if check_opponent[cell_row][cell_col] == "[ ]":
        did_hit = "Missed"
        marker = " o "
    elif check_opponent[cell_row][cell_col] == " x ":
        did_hit = "Already hit"
        marker = " x "
    elif check_opponent[cell_row][cell_col] == " o ":
        did_hit = "Already missed"
        marker = " o "
    else:
        did_hit = "Hit!"
        marker = " x "
        global player_score 
        player_score += 1
    player_shots.append([cell_row,cell_col,marker])
    for ship in range(len(opponent_board)):
        if opponent_board[ship][0] == cell_row and opponent_board[ship][1] == cell_col:
            opponent_board[ship][2] = marker
        else: 
            opponent_board.append([cell_row,cell_col,marker])
    print("--- Player shot at "+cell.upper()+" and "+did_hit+"---")
    opponent_shot()

def opponent_shot():
    # random opponent, does not check if shot before
    did_hit = ""
    marker = ""
    cell_row = random.randint(1,board_height)-1
    cell_col = random.randint(1,board_width)-1
    check_opponent = prep_board(player_board)
    if check_opponent[cell_row][cell_col] == "[ ]":
        did_hit = "Missed"
        marker = " o "
    elif check_opponent[cell_row][cell_col] == " x ":
        did_hit = "Already hit"
        marker = " x "
    elif check_opponent[cell_row][cell_col] == " o ":
        did_hit = "Already missed"
        marker = " o "
    else:
        did_hit = "Hit!"
        marker = " x "
        global opponent_score
        opponent_score += 1
    opponent_shots.append([cell_row,cell_col,marker])
    for ship in range(len(player_board)):
        if player_board[ship][0] == cell_row and player_board[ship][1] == cell_col:
            player_board[ship][2] = marker
        else: 
            player_board.append([cell_row,cell_col,marker])
    cell_name = str(index_to_letter[cell_col+1]).upper()+str(cell_row+1)
    print("--- Opponent shot at {cell_name} and {did_hit} ---".format(cell_name = cell_name, did_hit = did_hit))

def help_menu():
    print(
"""Help:
Try to sink your opponent's ships by entering a cell name to shoot at.
You can look at a map of your ships by entering 1. This will also show where your opponent has made shots.
You can look at a map of where your past shots have been made by entering 2. Try to narrow in on where your opponent's ships are.
Make a shot by entering 3 and inputting the cell you want to hit. Win by getting 17 points (all ships sunk).
When you're done, enter 0 to quit the game.

Ships: Car-Carrier, Bat-Battleship, Des-Destroyer, Sub-Submarine, Pat-Patrol Boat 
Legend: x-hit, o-miss, []-no information yet

Have fun!
""") 

print("Get ready to play Battleship!")
main_menu()
