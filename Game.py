
from asyncio.windows_events import NULL
from itertools import count
import math
import random
from unittest import result


def main_screen():
    print(' _________________________________________________________________')
    print("|  _____  _  ____     _____  _____ _____    ______ ______ _____   |")
    print("| /__ __\/ \/   _\   /__ __\/  _  \/   _\   /__ __\/  _  \/  __/  |")   
    print("|   / \  | ||  / _____ / \  | / \ ||  / _____ / \  | / \ ||  \    |")  
    print("|   | |  | ||  \_\____\| |  | |-| ||  \_\____\| |  | \_/ ||  /_   |") 
    print("|   \_/  \_/\____/     \_/  \_/ \_|\____/     \_/  \_____/\____\  |")
    print('|_________________________________________________________________|')
    print('|                                                                 |')
    print("|Press 1 to play with friend.                                     |")
    print("|Press 2 to play with Computer.                                   |")
    print("|Press 3 to exit.                                                 |")
    mode = input("|Enter your choice: ");
    return mode;

def cpu_menu():
    print("|------------------------------------------|")
    print("|              CPU AI Modes                |")
    print("|------------------------------------------|")
    print("|Press 1 to Play Easy Mode!                |")
    print("|Press 2 to Play Hard Mode!                |")
    print("|Press 3 to return to main menu!           |")
    mode = input("|Enter your choice: ")
    return mode;

# Display the game board to the screen
def display_board():

  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


def user_choice():
    while True:
        inp = input("[Player 1] Choose your mark [X/O]: ")
        if (inp.lower() == 'x'):
            print("[Player 1] choosed 'X' and [Player 2] choosed 'O'!")
            return 'X'
        elif (inp.lower() == 'o'):
            print("[Player 1] choosed 'O' and [Player 2] choosed 'X'!")
            return 'O'
        else:
            print("Enter correct input!")

def player_input(mark):
    while True:
        inp = input("Player '" + mark + "' Enter your choice: ")
        if (inp.isdigit() and int(inp) < 10 and int(inp) > 0 ):
            inp = int(inp)
            if board[inp-1] == '-':
                return inp
            else: 
                print("Player '" + mark + "' Place is already taken.")
        else:
            print("Player '" + mark + "' Enter valid option (1-9).")
            

def win_check(current_player):

    count = 0;
    for x in range(0,9):
        if( board[x] == '-'):
            count += 1;
    if count == 0:
        return NULL;
    # check rows!

    if board[0] == board[1] == board[2] and board[0] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[0] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    elif board[3] == board[4] == board[5] and board[3] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[3] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    elif board[6] == board[7] == board[8] and board[6] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[6] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    ## check columns!!
    elif board[0] == board[3] == board[6] and board[0] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[0] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    elif board[1] == board[4] == board[7] and board[1] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[1] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    elif board[2] == board[5] == board[8] and board[2] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[2] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    ## Check diagonals
    elif board[0] == board[4] == board[8] and board[0] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[0] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False

    elif board[2] == board[4] == board[6] and board[4] != "-":
        print("|--------------------------------------------|")
        print("|          Player '" + board[2] + "' Wins the game!         |")
        print("|--------------------------------------------|")
        return False
    else:
        return True

# def check_tie(cur):
#     count = 0;
#     for x in board:
#         if (x == '-'):
#             count += 1
#     if (count == 0):
#         return True
#     else:
#         return False

def check():
    count = 0;
    for x in board:
        if (x == '-'):
            count += 1
    if (count == 0):
        return 0

    if board[0] == board[1] == board[2] and board[0] != "-":
        return 1 if board[0] == 'X' else -1

    elif board[3] == board[4] == board[5] and board[3] != "-":
        return 1 if board[3] == 'X' else -1

    elif board[6] == board[7] == board[8] and board[6] != "-":
        return 1 if board[6] == 'X' else -1

    ## check columns!!
    elif board[0] == board[3] == board[6] and board[0] != "-":
        return 1 if board[0] == 'X' else -1

    elif board[1] == board[4] == board[7] and board[1] != "-":
        return 1 if board[1] == 'X' else -1

    elif board[2] == board[5] == board[8] and board[2] != "-":
        return 1 if board[2] == 'X' else -1

    ## Check diagonals
    elif board[0] == board[4] == board[8] and board[0] != "-":
        return 1 if board[0] == 'X' else -1

    elif board[2] == board[4] == board[6] and board[4] != "-":
        return 1 if board[2] == 'X' else -1   

# def checkWinner():
    
#     if (check() == 1):
#         return 1
#     elif (cur == 'O'):
#         return -1
#     if (check_tie(cur)):
#         return 0


def change_player(cur):
    if (cur == "X"):
        return "O";
    else:
        return "X";

def cpu_easy_input(cur):
    while True:
        position = random.randint(0, 8)
        if (board[position] == '-'):
            return position



def cpu_move(cur):
    bestScore = -math.inf;
    bestMove = None;
    if (cur == 'X'):
        ai = 'X'
        human = 'O'
    else:
        ai = 'O'
        human = 'X'

    for x in range(0,9):
        if( board[x] == '-'):
            board[x] = ai;
            score = minimax(board,0,False,ai,human); #false is for non-maximaizing player such as human
            board[x] = '-';
            if (score > bestScore):
                bestScore = score
                bestMove = x
            
    return bestMove;


def minimax(board,depth, ismaximizing,ai,human):
    
    if check() == 1:
        return 1
    if check() == -1:
        return -1
    if check() == 0:
        return 0
    
    #print("in minimax")
    # score = []
    # for x in range(0,9):
    #     if( board[x] == '-'):
    #         board[x] = cur;
    #         score.append(minimax(board,depth + 1,False,cur))  #false is for non-maximaizing player such as human
    #         board[x] = '-';
    # return max(score) if ismaximizing else min(score)

    if(ismaximizing):
        bestScore = -math.inf
        for x in range(0,9):
            if( board[x] == '-'):
                board[x] = ai;
                
                score = minimax(board,depth + 1,False,ai,human); #false is for non-maximaizing player such as human
                #print(score)
                board[x] = '-';
                bestScore = max(score, bestScore)
        return bestScore;
    else:
        bestScore = math.inf
        for x in range(0,9):
            if( board[x] == '-'):
                board[x] = human;
                
                score = minimax(board,depth + 1,True,ai,human); #false is for non-maximaizing player such as human
                #print(score)
                board[x] = '-';
                bestScore = min(score, bestScore)
        return bestScore;

         
def clear_board():
    for x in range(0,9):
        board[x] = '-'



def main_game():
    global board
    play = True
    board =['-','-','-','-','-','-','-','-','-']
    

    while play:
        mode = main_screen();
        
        if (mode == '1'):
            ## Player Mode.
            Manual_play = True
            player1 = user_choice();
            display_board();
            while Manual_play:
                
                current_player = player1;
                board_idx = player_input(current_player);
                board[board_idx-1] = current_player;
                display_board();
                Manual_play = win_check(current_player)
                if Manual_play:
                    current_player = change_player(current_player)
                    board_idx = player_input(current_player);
                    board[board_idx-1] = current_player;
                    display_board();
                    Manual_play = win_check(current_player);
            clear_board()

        elif (mode == '2'):
            #CPU mode
            cpu_mode = cpu_menu();
            if (cpu_mode == '1'):
                ## easy mode
                cpu_play = True
                player1  = user_choice();
                display_board();
                while cpu_play:

                    current_player = player1;
                    board_idx = player_input(current_player);
                    board[board_idx-1] = current_player;
                    display_board();
                    cpu_play = win_check(current_player)
                    if cpu_play:
                        board_idx = cpu_easy_input(current_player);
                        current_player = change_player(current_player)
                        board[board_idx] = current_player;
                        display_board();
                        cpu_play = win_check(current_player);

                clear_board()

            elif (cpu_mode == '2'):
                ## hard mode minimax algorithm
                print("CPU Plays First! Good Luck")
                cpu_play = True
                display_board();
                current_player = 'X'
                while cpu_play:
                    
                    board_idx = cpu_move(current_player)
                    board[board_idx] = current_player
                    display_board()
                    cpu_play = win_check(current_player)
                    if cpu_play:
                        current_player = change_player(current_player)
                        board_idx = player_input(current_player);
                        board[board_idx-1] = current_player;
                        display_board();
                        cpu_play = win_check(current_player)
                        current_player = change_player(current_player)
                        
            clear_board()



if __name__ == '__main__':
    main_game()