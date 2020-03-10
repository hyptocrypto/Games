from IPython.display import clear_output


# Print game board
def display_board(board):
    
    clear_output()
    

    print('\n')
    print(board[1]+' |'+board[2]+'|'+board[3])
    print('--|-|--')
    print(board[4]+' |'+board[5]+'|'+board[6])
    print('--|-|--')
    print(board[7]+' |'+board[8]+'|'+board[9])
    print('\n')



board = [' ']*10




# Function to let player choose to be X or O
def player_input():
     
    marker = ''
    
 
    
    while marker != 'X' and marker != 'O':
        marker = input('Player1, please choose to be x or o: ').upper()
        
    
    
    
    
    if marker == 'X':

        players = {'X':'Player 1', 'O': 'Player2'}
        markers = {'Player1' : 'X', 'Player2': 'O'}
    else:
        players = {'O':'Player 1', 'X': 'Player2'}
        markers = {'Player1' : 'O', 'Player2': 'X'}

    return players, markers


# Function that takes players input and appends it to the game board
def player_move(player, board):

    while True:
    
        move = input(f'{player}, please choose a spot:')
        if move in ['1','2','3','4','5','6','7','8','9']:
            move = int(move)

        spots = [1,2,3,4,5,6,7,8,9]
        if move in spots and board[move] == ' ':
            board[move] = player
            display_board(board)
            break
        else:
            print('Not valid spot')





# Function to check for all winning scenarios 
def check_win(players, board):
    indecies = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    game_over = False
    winner = None
    
    for index_combo in indecies:
        if board[index_combo[0]] == board[index_combo[1]] and board[index_combo[1]] == board[index_combo[2]]:
            if board[index_combo[0]] != ' ':
                winner = players[board[index_combo[0]]]
                game_over = True
                break
        
    return game_over, winner




# Main game function
def game():
    move = 0
    board=[' ']*10
    display_board(board)
    player_dict, marker_dict = player_input()
    game_over = False
    while game_over == False:
        if move % 2 == 0:
            player = marker_dict['Player1']
        else:
            player = marker_dict['Player2']
        player_move(player, board)
        move +=1
        game_over, winner = check_win(player_dict, board)
        
        if move > 8 and not game_over:
            break
    if game_over:
        
        print(f'{winner} wone!\n')
    else:
        print('Stalemate')



# Run main game fuction
if __name__ == '__main__':
    game()









