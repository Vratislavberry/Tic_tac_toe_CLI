from tic_tac_toe import Tic_tac_toe

game = Tic_tac_toe()


while True:
    game.update_board()
    print(f"Player \"{game.player_on_turn}\" is on the move")
    x, y = game.get_coordinates()
    game.make_turn(x, y)
    if game.game_ended():
        game.update_board()
        break
    game.switch_player()

end_of_game_reason = game.game_ended()
if end_of_game_reason == 1:
    print(f"The winner is: \"{game.winner}\"")
elif end_of_game_reason == 2:
    print("It's a draw")



