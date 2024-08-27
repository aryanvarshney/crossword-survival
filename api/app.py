from flask import Flask

app = Flask(__name__)

@app.route("/")
def start():
    return "<p>New Project<p>"

'''
Basic login page
In profile, let's add some basic tracking like how many games a user has played and best score
'''
@app.get('/login')
def login_get():
    return "show_the_login_form()"

@app.post('/login')
def login_post():
    return "do_the_login()"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

'''
This will be the endpoint for the session based game that users can play
POST: This will create the game session and start generating crossword puzzles
PUT: Whenever the user clicks submit, this will check if the crossword puzzle is correct and either move to the next one or tell the user some of the puzzle is wrong
'''
@app.post("/game/<int:game_id>")
def create_game(game_id: int):
    return "Create game"

@app.put("/game/<int:game_id>")
def update_game(game_id: int):
    return "Update game"


