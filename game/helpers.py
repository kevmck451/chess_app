# The mechanism i decide the friendly pieces vs enemy pieces is by checking if they are upper or lower
# Light Colored pieces are upper case, dark colored pieces are lower case
# Instead of rewriting the code for each color
# I can inverse the result when i call the function to check the legal move.
def sameColor(switcher,string):
    if switcher:
        return string.isupper()
    else:
        if string:
            return not string.isupper()

def oppositeColor(switcher,string):
    if  switcher:
        return  string.islower()
    else:
        if string:
            return not string.islower()

# i send and recieve the cords in 2 diget string for example 50
# first diget (5) is the y value, and second diget (0) is the x value
# instead of converting evertime while appending the available moves
# i send it here for to be less messy..
# instead of str(yCord-1)+str(xCord)  strC(yCord-1,xCord)
def strC(y, x):
    return str(y)+str(x)

# Dark Pieces move down
# Light Pieces move up
def pawnColorMoves(color):
    if color:
        direction = -1
        baseSquare = 6
    else:
        direction = 1
        baseSquare = 1
    return direction, baseSquare

def kingName(color):
    if color:
        return 'K'
    else:
        return 'k'

def piecesName(color):
    if color:
        queen = 'Q'
        rook = 'R'
        bishop = 'P'
    else:
        queen = 'q'
        rook = 'r'
        bishop = 'b' 
    return queen,rook,bishop

def is_valid_move(board, move):
    # Check if a move is valid on the current chess board
    pass

def is_checkmate(board, player):
    # Check if the current player is in checkmate
    pass

def get_legal_moves(board, piece):
    # Get a list of legal moves for a given chess piece
    pass

def initialize_board():
    # Create and initialize the chessboard
    pass

def update_board(board, move):
    # Update the board state after a valid move
    pass

def board_to_json(board):
    # Convert the board state to JSON for rendering
    pass

def resign_game(game, player):
    # Handle a player's resignation
    pass

def offer_draw(game, player):
    # Handle a player's draw offer
    pass

def suggest_move(board):
    # Provide a suggestion for the next move
    pass

def log_move_history(game, move):
    # Log the move in the game's history
    pass

def get_move_history(game):
    # Retrieve and format the game's move history
    pass

def validate_input(data):
    # Validate user input for moves and other actions
    pass

def handle_error(error_message):
    # Handle and display errors to the user
    pass

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'