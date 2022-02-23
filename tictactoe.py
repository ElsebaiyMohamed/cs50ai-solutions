"""
Tic Tac Toe Player
"""
import copy
from msilib.schema import Error


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    
    x = 0
    o = 0
    for row in board:
        for i in row:
            if i == X:
                x += 1
            elif i == O:
                o += 1
            else:
                continue
    if o <  x: 
        return O
    else: 
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = list()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] is EMPTY:   
                action.append((i,j))
    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    my_board = copy.deepcopy(board)
    if not terminal(my_board):
        i , j = action
        my_board[i][j] = player(my_board) # return X or O
        return my_board
    #return my_board
    raise Error("Invalid move")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    b = copy.deepcopy(board)
    
    # coulmn #1
    if b[0][0] == X and b[1][0] == X and b[2][0] == X:
        return X
    elif b[0][0] == O and b[1][0] == O and b[2][0] == O:
        return O
    #----------------------------------------------------
    # coulmn #2
    elif b[0][1] == X and b[1][1] == X and b[2][1] == X:
        return X
    elif b[0][1] == O and b[1][1] == O and b[2][1] == O:
        return O
    #----------------------------------------------------
    # coulmn #3
    elif b[0][2] == X and b[1][2] == X and b[2][2] == X:
        return X
    elif b[0][2] == O and b[1][2] == O and b[2][2] == O:
        return O
    #----------------------------------------------------
    # row #1
    elif b[0][0] == X and b[0][1] == X and b[0][2] == X:
        return X
    elif b[0][0] == O and b[0][1] == O and b[0][2] == O:
        return O
    #----------------------------------------------------
    # row #2
    elif b[1][0] == X and b[1][1] == X and b[1][2] == X:
        return X
    elif b[1][0] == O and b[1][1] == O and b[1][2] == O:
        return O
    #----------------------------------------------------
    # row #3
    elif b[2][0] == X and b[2][1] == X and b[2][2] == X:
        return X
    elif b[2][0] == O and b[2][1] == O and b[2][2] == O:
        return O
    #----------------------------------------------------
    # diagonal left
    elif b[0][0] == X and b[1][1] == X and b[2][2] == X:
        return X
    elif b[0][0] == O and b[1][1] == O and b[2][2] == O:
        return O
    #----------------------------------------------------
    # diagonal right
    elif b[0][2] == X and b[1][1] == X and b[2][0] == X:
        return X
    elif b[0][2] == O and b[1][1] == O and b[2][0] == O:
        return O
    #----------------------------------------------------

    else:
        return None

def terminal(game_board):
    """
    Returns True if game is over, False otherwise.
    """
    board = copy.deepcopy(game_board)
    case = winner(board)
    if case is not None or draw(board) :
        return True
    return False

def draw(game_board):
    board = copy.deepcopy(game_board)
    return board[0].count(EMPTY) == 0 and board[1].count(EMPTY) == 0 and board[2].count(EMPTY) == 0
    
def utility(game_board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    board = copy.deepcopy(game_board)
    case = winner(board)
    if case == X:
        return 1
    elif case == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    state = copy.deepcopy(board)
    
    return max_to_play(state)[1]

def max_to_play(game_state):
    
    state = copy.deepcopy(game_state)
    best_action = None

    if terminal(state):
        return utility(state), best_action
    v = -10
    for action in actions(state):
        new_v = min_to_play(result(state, action))
        if best_action is None:
            best_action = action
        if v > new_v:
            continue
        else:
            v = new_v
            best_action = action
        
    return v , best_action
                    
            
def min_to_play(game_state):
    state = copy.deepcopy(game_state)
    if terminal(state):
        return utility(state)
    
    v = 10 
    for action in actions(state):
        new_v = max_to_play(result(state, action))[0]
        v = min(new_v, v)
    return v