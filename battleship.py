# I will try to keep things organized
# imports (if any)

# dictionaries
index_to_letter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
letter_to_index = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
# global scope variables (if any)
play = True
board_width = 10
board_height = 10 
player_board = [[1,1,"Destroyer"], [1,2,"Destroyer"]]
opponent_board = []
player_shots = []
opponent_shots = []

# classes (if any)

# functions (if any)

def prep_blank_board():
    display_board = []
    for row in range(board_height):
        for col in range(board_width):
            display_board.append([row, "[ ]"])
    return display_board

def display_game_board(board):
    string_to_print = "   "
    for col in range(board_width):
        return
    for row in range(board_height):
        string_to_print += "\n"
        for col in range(board_width):
            string_to_print += " " + board[row][1]
    return string_to_print

# print(display_game_board(prep_blank_board()))

print(letter_to_index['a'])
