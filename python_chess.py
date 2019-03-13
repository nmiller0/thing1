import chess_py
from chess_py import Game, Human, color, Board

new_game = Game(Human(color.white), Human(color.black))

print(white_move())

result = new_game.play()

