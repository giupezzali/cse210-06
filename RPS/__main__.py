from game.director.director import Director
from game.casting.cast import Cast
from game.casting.choice import Choice
from game.casting.score import Score
from game.casting.lives import Lives


# create the cast
cast = Cast()
cast.add_actor("choices", Choice())
cast.add_actor("scores", Score())
cast.add_actor("scores", Score())
cast.add_actor("lives", Lives())

#start the game 
director = Director()
director.start_game(cast)