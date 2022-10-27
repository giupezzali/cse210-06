from game.casting.cast import Cast
from game.scripting.handle_posible_victory import HandlePossibleVictory
from game.scripting.handle_rounds import HandleRounds
from game.services.terminal_service import TerminalService
from game.casting.choice import Choice
from game.casting.lives import Lives
from colorama import Fore, Back, Style

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
        user_input: For the user's choice 
        self._handle_possible_victory: Verifies who wins.
        self._handle_rounds: Verifies who win the round. 
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self.user_input = '' 
        self._handle_possible_victory = HandlePossibleVictory()
        self._handle_rounds = HandleRounds()
        
    def start_game(self, cast):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
            cast (Cast): The cast of Actors in the game.
        """
        self._terminal_service.write_text('\nWelcome to Rock, Paper, Scissors! \n')
        self._terminal_service.write_text(Fore.CYAN + 'Round One!')

        while self._is_playing:
            for i in range(3):
                self._get_inputs()
                self._do_updates(cast)
            self._do_outputs(cast)
            self.is_playing(cast)

        if not self._is_playing:
            self._terminal_service.write_text('\n---------------------------------------')
            self._terminal_service.write_text('\nGood game! Thanks for playing! :D\n')
            self._terminal_service.write_text('---------------------------------------\n')


    def _get_inputs(self):
        """Ask for player's choice and return it to update the game.

        Args:
            self (Director): An instance of Director.
        """
        self.user_input = self._terminal_service.read_text('\nEnter a choice [rock, paper, scissors]: ')
        return self.user_input

    def _do_updates(self, cast):
        """Updates and handle possible victories.

        Args:
            self (Director): An instance of Director.
            cast (Cast): The cast of Actors in the game.
        """
        self._handle_possible_victory.execute(cast,self.user_input)
        
        
        
    def _do_outputs(self, cast):
        """handle rounds to give an output.

        Args:
            self (Director): An instance of Director.
            cast (Cast): The cast of Actors in the game.
        """
        self._handle_rounds.execute(cast)
            
    
    def is_playing(self, cast):
        """whether the game is playing or not.

        Args:
            self (Director): An instance of Director.
            cast (Cast): The cast of Actors in the game.
        """
        lives = cast.get_first_actor('lives')
        self._is_playing = lives.get_lives() > 0