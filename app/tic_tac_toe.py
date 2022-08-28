# start_game creates a model of tic-tac-toe
import json


def create_board(board_size):
    return json.dumps(dict(zip([i for i in range(1, board_size**2 + 1)], "-"*(board_size**2))))


# @param board_size - length of the side of a tic-tac-toe board
# @param num_players - number of players for tic-tac-toe game
def start_game(board_size, num_players):
    players = {}
    for i in range(1, num_players + 1):
        players[i] = '-'
    game = {'board': create_board(board_size), 'players': players, 'board_size': board_size, 'winner': '-'}
    return game


# similar to start_game, but reset_game keeps the same board_size and num_players as the previous game
def reset_game(game):
    return start_game(game['board_size'], len(game['players']))


def join_game(game, player):
    if player in game['players'] and game['players'].get(player) == '-':
        game['players'] = []
        return game
    else:
        return 'Player cannot be selected'


def make_move(game, player, move):
    board = json.loads(game['board'])
    if valid_move():
        board[move] = player
        game['players'][player].add(move)
        # check if win
        return game
    return 'Move was not valid'


def check_win(board, player, board_size):
    # vertical wins
    for i in range(1, board_size + 1):
        if board[i] == player:
            for n in range(1, board_size):
                if board[i + board_size * n] != player:
                    continue
                elif n == (board_size - 1):
                    return player

    # horizontal wins
    for i in range(0, board_size):
        if board[1 + board_size * i] == player:
            for n in range(2, board_size + 1):
                if board[i * board_size + n] != player:
                    continue
                elif n == board_size:
                    return player

    #diag down
    for i in range(0, board_size):
        if board[board_size * i + i + 1] != player:
            continue
        elif i == board_size - 1:
            return player

    #diag up
    for i in range(1, board_size + 1):
        if board[board_size * i - i + 1] != player:
            continue
        elif i == board_size - 1:
            return player
    return False


# checks 1) if it's player's turn, 2) if move is available
def valid_move():
    return True
