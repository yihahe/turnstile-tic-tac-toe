# Turnstile Tic-Tac-Toe

Turnstile Tic-Tac-Toe has a Flask API paired with a Redis DB. To run Turnstile Tic-Tac-Toe locally, you will need to be able to run redis-server (with json support). more documentation on that is found here: 
https://redis.io/docs/stack/json/

You can also run using Docker. The latest production docker image for turnstile-tic-tac-toe is available to pull here:
docker pull yihahe/turnstile:latest

Documentation on currently available endpoints can be found here after running app/flask_home.py: http://127.0.0.1:5000/api/docs

**New Game**
----
  _Allows users to create new game with default or custom parameters._

  _game/new_game_

  `GET` | `POST`

* **Data Params**

  _{'board_dimensions': <optional_int>,
    'num_players': <optional_int>'}_
  
  _default values for board_dimensions is 3 and num_players is 2._
  
**Reset Game**
----
  _Allows user to reset game given a game_id._

  _game/{game_id}/reset_game_

  `GET`

*  **URL Params**

   **Required:**
 
   `game_id=[integer]`
  
  _this will error unless a game_id is provided._
  
**Join Game**
----
  _Allows user to join a game given a game_id. Will allow users to join games until a game is filled._

  _game/{game_id}/join_game_

  `GET`

*  **URL Params**

   **Required:**
 
   `game_id=[integer]`
  
  _this will error unless a game_id is provided._ 

**Move**
----
  _Allows user to make a move given a game_id and player_id._

  _game/{game_id}/{player_id}_

  `GET`

*  **URL Params**

   **Required:**
 
   `game_id=[integer]`
   `player_id=[integer]`
  
* **Data Params**

  _{'move': <required_int>}_
  
  _a move is expected to be between 1 and board_size**2._
