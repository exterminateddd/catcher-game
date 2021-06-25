from Game import Game, Field
from P import P


game = Game(Field())
game.add_msg('Game started! First bonus - 2 points!')
game.set_bonus(2)

game.output()

while True:
    x, y = [int(i) for i in input('Точка ( x y )').strip().split(' ')]
    try_ = game.field.try_to_catch(P(x-1, y-1))
    if try_:
        if game.field.field[y-1][x-1].hidden:
            game.add_msg(f'Caught hidden! +{10 + game.current_bonus}')
            game.increase_count(10)
        else:
            game.add_msg(f'Caught! +{1+game.current_bonus}')
            game.increase_count(1)
        if len(game.get_caught_points()) in [3, 7, 15, 33, 42, 58, 64, 70]:
            game.set_bonus(5)
            game.add_msg(f'Reached {len(game.get_caught_points())} caught points! Bonus - 5!')
        else:
            game.set_bonus(0)
    else:
        game.add_msg('Not caught... -1')
        game.decrease_count()
    game.output()
