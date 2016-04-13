#Timothy Swain
#Week 4 Assignment Tic-Tac-Toe
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    return ((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or
            (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
            (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
            (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or
            (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or
            (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or
            (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or
            (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player
             
def startGame(startingPlayer, board):
    turn = startingPlayer 
    for player in range(0,9): #There are only 9 squares so there can be a maximum of 9 turns
        printBoard(board) #Calls and passes Board
        print('Turn for ' + player + '. Move on which space?') #Asks the player to pick a space
        move = input() #Player picks a spot on the board
        board[move] = turn #Records the position
        if( checkWinner(board, 'X') ): #checks if X has 3 in a row
            print('X wins!') #prints x wins
            break #breaks out of the function
        elif ( checkWinner(board, 'O') ): #checks if O has 3 in a row
            print('O wins!') #prints o wins
            break #breaks out of the function
    
        if turn == 'X': #If its X turn 
            turn = 'O' #changes to O's turn
        else:
            turn = 'X' #otherwise its X's turn
     printBoard(board)
