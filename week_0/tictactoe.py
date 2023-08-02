"""
Tic Tac Toe Player
"""

import copy

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
    move = 0
    for row in board:
        for item in row:
            if item == X:
                move += 1
            elif item == O:
                move -= 1
    if move == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i , j = action
    if new_board[i][j] != EMPTY:
        raise Exception
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check horizontal results
    for row in board:
        if row.count(X) == len(row):
            return X
        if row.count(O) == len(row):
            return O
    # Check number of columns
    for row in board:
        column_no = len(row)
    # Check for vertical results
    for col in range(column_no):
        column = []
        for row in range(len(board)):
            column.append(board[row][col])
        if column.count(X) == len(column):
            return X
        if column.count(O) == len(column):
            return O
    # Check for diagonal results
    main_diagonal = []
    anti_diagonal = []
    for i in range(len(board)):
        main_diagonal.append(board[i][i])
        anti_diagonal.append(board[i][len(board)-1-i])
    if main_diagonal.count(X) == len(main_diagonal):
        return X
    if main_diagonal.count(O) == len(main_diagonal):
        return O
    if anti_diagonal.count(X) == len(anti_diagonal):
        return X
    if anti_diagonal.count(O) == len(anti_diagonal):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Winner case
    if winner(board) is not None:
        return True
    # Check number of columns
    for row in board:
        column_no = len(row)
    # No more moves case
    for i in range(len(board)):
        for j in range(column_no):
            if board[i][j] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If game is over
    if terminal(board):
        return None
    current_player = player(board)
    # Max player scenario
    if current_player == X:
        # Set worst case scenario (if the Min player wins, utility value will be -1)
        # Nothing smaller can be achieved
        min_edge_utility = -2
        # Check all the actions
        for action in actions(board):
            # Produce new board from taken action
            new_board = result(board, action)
            # Check what move Min player would do with new_board
            min_player_utility = min_value(new_board)
            if min_player_utility > min_edge_utility:
                min_edge_utility = min_player_utility
                best_action = action
    # Min player scenario
    if current_player == O:
        # Set worst case scenario (if the Max player wins, utility value will be 1)
        # Nothing smaller can be achieved
        max_edge_utility = 2
        # Check all the actions
        for action in actions(board):
            # Produce new board from taken action
            new_board = result(board, action)
            # Check what move Min player would do with new_board
            max_player_utility = max_value(new_board)
            if max_player_utility < max_edge_utility:
                max_edge_utility = max_player_utility
                best_action = action
    return best_action


def max_value(board):
    '''Returns best value (highest possible score) for Max player'''
    # Set worst case scenario (if the Min player wins, utility value will be -1)
    # Nothing smaller can be achieved
    v = -2
    # If game is over (all the possible actions have been checked)
    if terminal(board):
        return utility(board)
    # If game is not over, look for the best value
    # Check all the actions
    for action in actions(board):
        # Produce new board from taken action
        new_board = result(board, action)
        # Check what move Min player would do with new_board
        # And compare min_edge_utility with utility of Min player move
        # Choose the bigger value
        v = max(v, min_value(new_board))
    return v
    

def min_value(board):
    '''Returns best value (lowest possible score) for Min player'''
    # Set worst case scenario (if the Max player wins, utility value will be 1)
    # Nothing bigger can be achieved
    v = 2
    # If game is over (all the possible actions have been checked)
    if terminal(board):
        return utility(board)
    # If game is not over, look for the best value
    # Check all the actions
    for action in actions(board):
        # Produce new board from taken action
        new_board = result(board, action)
        # Check what move Max player would do with new_board
        # And compare min_edge_utility with utility of Max player move
        # Choose the smaller value
        v = min(v, max_value(new_board))
    return v

