from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player


@app.route('/')
def index():
    return render_template('index.html', title="Let's Play Rock Paper Scissors")

@app.route('/result', methods=['post'])
def player_form():
    player1_selection = request.form['player1-selection']
    player2_selection = request.form['player2-selection']
    player1 = Player("Player 1", player1_selection)
    player2 = Player("Player 2", player2_selection)
    player_choices = Game(player1_selection, player2_selection)

    if player_choices.player1_choice == player_choices.player2_choice:
            print("Cool")

    return render_template('result.html', title='The Results are in...', player1=player1, player2=player2)