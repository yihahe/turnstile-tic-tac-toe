from flask import Flask, request, render_template
from rejson import Client, Path
from app import tic_tac_toe as ttt

app = Flask(__name__)
rj = Client(host='localhost', port=6379, decode_responses=True)


@app.route('/')
def hello():
    return 'Welcome to Turnstile Tic Tac Toe!'


@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')


@app.route('/game/new_game', methods=['POST', 'GET'])
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


@app.route('/game/<game_id>/reset_game', methods=['GET'])
def reset_game(game_id):
    game = rj.jsonget(game_id, Path.rootPath())
    rj.jsonset(game_id, Path.rootPath(), ttt.reset_game(game))
    return f'Your game {game_id} has reset'


@app.route('/game/<game_id>/join_game', methods=['GET'])
def join_game(game_id):
    game = rj.jsonget(game_id, Path.rootPath())
    game, message = ttt.join_game(game)
    rj.jsonset(game_id, Path.rootPath(), game)
    return message


@app.route('/game/<game_id>/<player_id>', methods=['POST'])
def play_game(game_id, player_id):
    game = rj.jsonget(game_id, Path.rootPath())
    if game['winner'] != '-':
        return f"{game['winner']} has already won."
    move = request.json['move'] if 'move' in request.json else 0
    game, message = ttt.make_move(game, player_id, move)
    rj.jsonset(game_id, Path.rootPath(), game)
    return message


if __name__ == '__main__':
    app.run(debug=True)
