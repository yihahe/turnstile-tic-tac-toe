from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
redis_client = FlaskRedis(app)


@app.route('/')
def hello():
    return 'Welcome to Turnstile Tic Tac Toe!'


if __name__ == '__main__':
    app = Flask(__name__)
    redis_client.init_app(app)
