class Lives:
    """Available lives in the game

    Attributes:
        _lives(int): Available lifes for the game.
    """
    def __init__(self):
        """Constructs a new set of lives.

        Args:
            self (lives): An instance of Lives.
        """
        self._lives = 3

    def get_lives(self):
        """Gets available lifes.
        
        Returns: lives(int)
        """
        return self._lives 

    def set_lives(self, lives):
        """Modify the lives attribute
        """
        self._lives=lives


