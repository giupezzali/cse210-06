from re import T
from game.casting.cast import Cast
from game.scripting.action import Action
from game.services.terminal_service import TerminalService
from colorama import Fore, Back, Style

class HandleRounds(Action):
    
    def __init__(self):
        """Constructs a new HandleRounds."""
        self._terminal_service = TerminalService()

    def execute(self, cast):
        """Executes the handle rounds.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._calculate_score(cast)

    def _calculate_score(self, cast):
        """Calculate scores to see who wins the round

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor('scores')
        computer_score = cast.get_second_actor('scores')

        if (score.get_score() >= 2) and (computer_score.get_score() <= 1):
            self._terminal_service.write_text('\nCongratulations, you win this round!')
        elif (score.get_score() <= 1) and (computer_score.get_score() >= 2):
            self._terminal_service.write_text('\nYou lost this round. Better luck next time :(')
        elif (score.get_score() == 1) and (computer_score.get_score() == 1):
            self._terminal_service.write_text('\nIt is a tie!')

        score.set_score(0)
        computer_score.set_score(0)    
        lives = cast.get_first_actor('lives')
        lives.set_lives(lives.get_lives() - 1)

        if lives.get_lives() == 2:
            self._terminal_service.write_text(Fore.GREEN +'\nRound Two!')
        elif lives.get_lives() == 1:
            self._terminal_service.write_text(Fore.LIGHTMAGENTA_EX +'\nLast Round!')
        