# start_game creates a model of tic-tac-toe
import json
from app.utils import json_keys_int


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


# similar to start_game, reset_game keeps the same board_size and num_players as the previous game
def reset_game(game):
    return start_game(game['board_size'], len(game['players']))


# join_game allows players to join a game if there are any players available
def join_game(game):
    for player in game['players']:
        if game['players'].get(player) == '-':
            game['players'][player] = []
            return game, f'Your player id is {player}'
    else:
        return game, 'No player is available'


# make_move allows specific players to make valid moves
def make_move(game, player, move):
    board = json.loads(game['board'], object_hook=json_keys_int)
    if players_turn(game['players'], player) and valid_move(move, board):
        board[move] = player
        game['board'] = json.dumps(board)
        game['players'][player].append(move)
        winner = check_win(board, player, game['board_size'])
        if winner:
            game['winner'] = winner
            return game, f'Congratulations {winner}'
        return game, 'Move done'
    return game, 'Move is not valid'


def check_win(board, player, board_size):
    # vertical wins
    for i in range(1, board_size + 1):
        if board[i] == player:
            for n in range(1, board_size):
                print(i + board_size * n)
                if board[i + board_size * n] != player:
                    break
                elif n == (board_size - 1):
                    return player

    # horizontal wins
    for i in range(0, board_size):
        if board[1 + board_size * i] == player:
            for n in range(2, board_size + 1):
                if board[i * board_size + n] != player:
                    break
                elif n == board_size:
                    return player

    # diag down win
    for i in range(0, board_size):
        if board[board_size * i + i + 1] != player:
            break
        elif i == board_size - 1:
            return player

    # diag up win
    for i in range(1, board_size + 1):
        if board[board_size * i - i + 1] != player:
            break
        elif i == board_size - 1:
            return player
    return False


def players_turn(players, curr_player):
    num_moves_curr = len(players[curr_player])
    for player_id in players:
        # it is not a player's turn to play if
        # 1) not all players are registered yet
        # 2) they have played more moves than other players
        # 3) they have played the same amount of moves, but other players are supposed to go first
        if players[player_id] == '-' or \
                num_moves_curr > len(players[player_id]) or \
                (num_moves_curr == len(players[player_id]) and curr_player > player_id):
            return False
    return True


def valid_move(move, board):
    if move in board and board[move] == '-':
        return True
    return False
