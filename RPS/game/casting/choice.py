import random
from select import select

class Choice:
    """ A choice that can be a rock, paper or scissors.
    The responsibiliy of a puzzle is to display a secret word, represented as underscores and replace with a word when the user guesses.
    
    Attributes:
        _choices (list[str]): A list of possible choices
        _choice_selected (str): For a random choice from the list of choices
    """

    def __init__(self):
        """Constructs a new Choice.

        Args:
            self (Choice): An instance of Choice.
        """
        self._choices = ['rock', 'paper', 'scissors']
        self._choice_selected = ''
        self.random_choice()
        

    def get_choice(self):
        """Gets the choice.
        
        Returns: the selected choice.
        """
        return self._choice_selected
    
    def random_choice(self):
        ""
        self._choice_selected = random.choice(self._choices)
