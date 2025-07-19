import os # Used for clearing the console

# --- Global Variables ---
# The game board, represented as a list.
# Each number corresponds to a position on the board.
# Initialized with empty spaces.
board = [' ' for x in range(10)] # We'll ignore index 0 to make 1-9 mapping intuitive

# --- Functions ---

def display_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.
    The board is visualized as a 3x3 grid.
    """
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the console for a clean board display
    print('\n')
    print('     |     |')
    print('  {}  |  {}  |  {} '.format(board[1], board[2], board[3]))
    print('_____|_____|_____')
    print('     |     |')
    print('  {}  |  {}  |  {} '.format(board[4], board[5], board[6]))
    print('_____|_____|_____')
    print('     |     |')
    print('  {}  |  {}  |  {} '.format(board[7], board[8], board[9]))
    print('     |     |')
    print('\n')

def player_input():
    """
    Allows players to choose their marker (X or O).
    Returns a tuple with (Player 1 marker, Player 2 marker).
    """
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    """
    Places the given marker (X or O) on the board at the specified position.
    """
    board[position] = marker

def win_check(board, mark):
    """
    Checks if the given marker has won the game.
    Checks all rows, columns, and diagonals.
    """
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board, position):
    """
    Checks if a chosen position on the board is free.
    Returns True if the space is empty, False otherwise.
    """
    return board[position] == ' '

def full_board_check(board):
    """
    Checks if the board is full.
    Returns True if the board is full (a draw), False otherwise.
    """
    for i in range(1, 10):
        if space_check(board, i):
            return False # If any space is found, the board is not full
    return True # If loop completes, no empty spaces were found

def player_choice(board):
    """
    Asks the player for their next position (1-9) and validates the input.
    Ensures the input is a digit and the space is free.
    """
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose your next position: (1-9) '))
        except ValueError:
            print("That's not a number! Please enter a number between 1 and 9.")
            continue # Continue loop to ask for input again
        if position not in range(1, 10):
            print("Invalid position! Please enter a number between 1 and 9.")
        elif not space_check(board, position):
            print('This space is already taken! Choose another spot.')
    return position

def replay():
    """
    Asks the player if they want to play again.
    Returns True if they do, False otherwise.
    """
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# --- Main Game Logic ---

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = 'Player 1' # Player 1 always goes first

    print(f"{turn} will go first!")

    game_on = True # Flag to control the game loop

    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 2' # Switch turns
        else:
            # Player 2's turn
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations Player 2! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 1' # Switch turns

    if not replay():
        break # Exit the main game loop if players don't want to play again


