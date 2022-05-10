import commongamefunctions as cgf
import random


def instruction():
    """ Display the instructions for tic tac toe to the user to use this function simply type instructions() """
    print(
            """
                 Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
                 This will be a showdown between your human brain and my silicon processor.
                 You will make your move known by entering a number, 0 - 8. The number
                 will correspond to the board position as illustrated:
    
                            1 | 2 | 3
                            ---------
                            4 | 5 | 6
                            ---------
                            7 | 8 | 9
    
                Prepare yourself, human. The ultimate battle is about to begin. \n
                """)


instruction()
# function list
#display instruction
#new board
def new_board():
    """define a new board"""
    board = []
    for i in range(MAX_SQUARES):
        board.append(EMPTY_TOKEN)
    return board
#ask yes no or flip coin ask number
def ask_yes_no():
    pass
def flip_coin():
    """flips a coin and returns the results of Heads or Tails"""
    import random
    results = None
    choices = ["Heads","Tails"]
    results = random.choice(choices)
    return results

def ask_number_in_range(question,low,high):
    """ask the user to choose a number within a given range and return the number if it is a good value"""
    while True:
        number = input(question)
        try:
            number = int(number)
            if number >= low:
                if number <= high:
                    return number
                else:
                    print("that number is too high")
            else:
                print("that number is too low")
        except:
            print("not a good number")
#assign pieces
def pieces():
    global human_player
    global comp_player
    answer = cgf.ask_yes_no("would you like to go first")
    if answer =="yes":
        print("you will need it")
        human_player = X_TOKEN
        comp_player = O_TOKEN
    else:
        print("big mistake you stand no chance")
        human_player = O_TOKEN
        comp_player = X_TOKEN
# display board current
def display_board(gameboard):
    """displaying the board"""
    print(str.format("""
     {} | {} | {}
    -----------
     {} | {} | {}
    -----------
     {} | {} | {}
    """,gameboard[0],gameboard[1],gameboard[2],gameboard[3],
                     gameboard[4],gameboard[5],gameboard[6],
                     gameboard[7],gameboard[8]))
# legal moves
def legal_moves(board):
    moves = []
    for place in range(MAX_SQUARES):
        if board[place] == EMPTY_TOKEN:
            moves.append(place)
    return moves

# check for winner
def check_winner(board):
    wins = [(0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6)]
    Winner = None

    for row in wins:
        if board [row[0]] == board[row[1]] == board[row[2]] != EMPTY_TOKEN:
            winner = board[row[0]]
            return winner
    if EMPTY_TOKEN not in board:
        winner = "TIE"
# human move
def human_moves(board):
    while True:
        spot = cgf.ask_number_in_range("where would you like to place your piece",1,9)
        spot = spot - 1
        if board[spot] == EMPTY_TOKEN:
            board[spot] = human_player
            break
        else:
            print("you cant go there ")

#computer move
def comp_move(diff,board):
    pos_moves = legal_moves(board)
    temp_board = board[:]
    moves = legal_moves(board)
    if diff == "Easy":
        spot = random.choice(pos_moves)
        board[spot] = comp_player
    elif diff == "medium":
        BEST_MOVES = [4,1,7,3,5,0,2,6,8]
        #checking if comp can win
        for move in pos_moves:
            board[move] = comp_player
            if check_winner(board) == comp_player:
                spot = move
                print("now its my turn to show you how to play I place my" +comp_player + "at" +str(spot+1))
                board[move] = comp_player
                return
            else:
                temp_board[move] = EMPTY_TOKEN

        # checking if player can win
        for move in pos_moves:
            board[move] = human_player
            if check_winner(board) == human_player:
                spot = move
                print("now its my turn to show you how to play I place my" + human_player + "at" + str(spot + 1))
                board[move] = human_player
                return
            else:
                temp_board[move] = EMPTY_TOKEN
        #place best move if com and human cant win
        for move in BEST_MOVES:
            if move in pos_moves:
                spot = move
                print("now its my turn to show you how to play I place my" + human_player + "at" + str(spot + 1))
                board[move] = human_player

    elif diff == "hard":
        #ADD A "INT" STATMENT
        BEST_MOVES = [4, 1, 7, 3, 5, 0, 2, 6, 8]
        # checking if comp can win
        for move in pos_moves:
            board[move] = comp_player
            if check_winner(board) == comp_player:
                spot = move
                print("now its my turn to show you how to play I place my" + comp_player + "at" + str(spot + 1))
                board[move] = comp_player
                return
            else:
                temp_board[move] = EMPTY_TOKEN

        # checking if player can win
        for move in pos_moves:
            board[move] = human_player
            if check_winner(board) == human_player:
                spot = move
                print("now its my turn to show you how to play I place my" + human_player + "at" + str(spot + 1))
                board[move] = human_player
                return
            else:
                temp_board[move] = EMPTY_TOKEN

        # place best move if com and human cant win
        for move in BEST_MOVES:
            if move in pos_moves:
                spot = move
                print("now its my turn to show you how to play I place my" + human_player + "at" + str(spot + 1))
                board[move] = human_player




#switching turns
def switch_turn(turn):
    if turn == X_TOKEN:
        turn = O_TOKEN
    else:
        turn = X_TOKEN
    return turn
# congrats the winner
def congrats_winner(winner,comp_player,human_player):
    if winner != "TIE":
        print(winner,"has won!\n")
    else:
        print("its a TIE\n")
    if winner == comp_player:
        #dio winning with the wrryyy
        print("i won moral being")
    elif winner == human_player:
        #dio finding out jotaro can move
        print("impossible")
    else:
        print("a tie patheice")

def pick_from_menu(question,option):
    while True:
        for i in range(len(option)):
            print(str.format("\t{0} ...... {1:<30}", i + 1, option[i]))
        choice = input("what would you like to do? ")
        if choice.isnumeric():
            if int(choice) <= len(option):
                choice = int(choice)
                return choice
            else:
                print("thats not a option")

MAX_SQUARES = 9
EMPTY_TOKEN = " "
X_TOKEN = "X"
O_TOKEN = "O"
human_player = " "
comp_player = " "
turn = X_TOKEN

def main():
    options = ["Easy","medium","hard"]
    diff = cgf.pick_from_menu("choose your difficulty",options)
    if diff == 1:
        diff = options[diff -1]
    else:
        diff = "easy"

    #display the game instructions
    instruction()

    #create an empty tic tac toe board
    gameboard = new_board()
    moves = legal_moves(gameboard)
    print(moves)
    pieces()
    global turn
    winner = None
    display_board(gameboard)
    while not winner:
        if turn == human_player:
            print(human_player + "Turn")
            human_moves(gameboard)
        else:
            print(comp_player + "Turn")
            comp_move(gameboard)

        winner = check_winner(gameboard)
        turn = switch_turn(turn)
        display_board(gameboard)

    congrats_winner(winner,comp_player,human_player)



    # determine who goes first
    # while playing (no players has got 3 in a row and board still has empty squares)
    # if turn was x
    # got x move
    # placed x token // update board
    # else
    # get 0 move
    # place o token // update board
    # switch turns
    # congratulation the winner or declare a tie



main()