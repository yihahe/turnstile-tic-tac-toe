# start_game creates a model of tic-tac-toe
import json


def start_game(board_size, num_players):
    players = {}
    for i in range(1, num_players + 1):
        players[i] = '-'
    game = {'board': create_board(board_size), 'players': players, 'board_size': board_size}
    return game


def reset_game(game):
    return start_game(game['board_size'], len(game['players']))


def create_board(board_size):
    return json.dumps(dict(zip([i for i in range(1, board_size**2 + 1)], "-"*(board_size**2))))


def make_move(game_id, player_id):
    if valid_move():
        # avail_moves def
        # check if win
        return True
    return False


def check_win(game, player_id):
    # board_size = game[avail_moves].size + game[player_x].size + game[player_y].size
    # vertical, horizontal, diag_down, diag_up
    # vertical
    # n = sqrt(board_size)
    # for i in range(1, n):
    # if player has i :
    # then check all i + n * range(1, n-1)

    # horizontal
    # for i in range(0, n-1):
    # if player has n*i + 1:
    # then check all i * n + range(2, n-1)

    #diag down
    # 1, 5, 9
    # if player has n*i + i + 1 for i in range(0, n-1)

    #diag up
    #3, 5, 7
    # if player has n*i - i + 1 for i in range (1, n)
    return True


# checks 1) if it's player's turn, 2) if move is available
def valid_move():
    return False
