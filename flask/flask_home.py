from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to Turnstile Tic Tac Toe!'


if __name__ == '__main__':
    app.run(debug=True)
