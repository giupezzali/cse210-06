from game.casting.cast import Cast
from game.scripting.action import Action
from game.services.terminal_service import TerminalService
from colorama import Fore, Back, Style

class HandlePossibleVictory(Action):
    
    def __init__(self):
        """Constructs a new HandlePossibleVictory."""
        self._is_game_over = False
        self.terminal_service = TerminalService()

    def execute(self, cast, user_input):
        """Executes the handle possible victory.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._handle_possible_victory(cast,user_input)

    def _handle_possible_victory(self,cast, user_input):
        """compare user option and the random choice to determine who wins.

        Args:
            cast (Cast): The cast of Actors in the game.
            user_input: a user's choice
        """
        choice = cast.get_first_actor('choices')
        choice.random_choice()
        object = choice.get_choice()
        score = cast.get_first_actor('scores')
        computer_score = cast.get_second_actor('scores')
        user_input = user_input.lower()
        if object != user_input:
            if user_input == 'rock':
                if object == 'scissors':
                    self.terminal_service.write_text('Rock smashes scissors! You win!')
                    score.set_score(score.get_score() + 1)
                else:
                    self.terminal_service.write_text('Paper covers rock! You lose.')
                    computer_score.set_score(computer_score.get_score() + 1)
            elif user_input == 'paper':
                if object == 'rock':
                    self.terminal_service.write_text('Paper covers rock! You win!')
                    score.set_score(score.get_score() +1)
                else:
                    self.terminal_service.write_text('Scissors cuts paper! You lose.')
                    computer_score.set_score(computer_score.get_score() + 1)
            elif user_input == 'scissors':
                if object == 'paper':
                    self.terminal_service.write_text('Scissors cuts paper! You win!')
                    score.set_score(score.get_score() +1)
                else:
                    self.terminal_service.write_text('Rock smashes scissors! You lose.')
                    computer_score.set_score(computer_score.get_score() + 1)
            else:
                print('Oops, something went wrong. Try again!')
        else:
            self.terminal_service.write_text(f'Both players selected {user_input}. It is a tie!')
        


