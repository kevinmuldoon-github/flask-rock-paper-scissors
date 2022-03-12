
from models.game import *

def who_wins(players, selections):

    player1 = players[0].name
    player2 = players[1].name

    player1_weapon = selections.player1_choice
    player2_weapon = selections.player2_choice
    
    if player1_weapon== "Rock":
        if player2_weapon == "Scissors":
            return player1
        elif player2_weapon == "Paper":
            return player2
    elif player1_weapon == "Scissors":
        if player2_weapon == "Paper":
            return player1
        elif player2_weapon == "Rock":
            return player2
    elif player1_weapon == "Paper":
        if player2_weapon == "Rock":
            return player1
        elif player2_weapon == "Scissors":
            return player2
    else:
        return None
