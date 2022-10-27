class Score:
    """Game score tracking

    Attributes:
        _score(int): Score.
        """
    def __init__(self):
        self._score = 0

    def get_score(self):
        """Gets the current score.
        
        Returns: score(int)
        """
        return self._score
    

    
    def set_score(self, score):
        """Modify the _score attribute
        """
        self._score=score