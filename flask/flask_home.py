from flask import Flask, request
from rejson import Client, Path
from app import tic_tac_toe as ttt

app = Flask(__name__)
rj = Client(host='localhost', port=6379, decode_responses=True)


@app.route('/')
def hello():
    return 'Welcome to Turnstile Tic Tac Toe!'


@app.route('/new_game', methods=['POST', 'GET'])
def new_game():
    # default tic-tac-toe settings with auto-incrementing game_id
    board_dimensions = 3
    num_players = 2
    game_id = rj.dbsize() + 1

    if request.method == 'POST':
        board_dimensions = request.json['board_dimensions'] if 'board_dimensions' in request.json else board_dimensions
        num_players = request.json['num_players'] if 'num_players' in request.json else num_players
    rj.jsonset(game_id, Path.rootPath(), ttt.start_game(board_dimensions, num_players))
    return f'Your game id is {game_id}'


if __name__ == '__main__':
    app.run(debug=True)
