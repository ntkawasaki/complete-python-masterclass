class Player(object):
    """Player class."""

    def __init__(self, name):
        """Initialize attributes."""

        self.name = name.title()
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        """Getter."""

        return self._lives

    def _set_lives(self, lives):
        """Setter."""

        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be below 0")
            self._lives = 0

    def _get_level(self):
        """Getter."""

        return self._level

    def _set_level(self, level):
        """Setter."""

        if level > 1:
            delta = level - self.level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level can't be less than 1.")

    lives = property(_get_lives, _set_lives)  # never use parentheses when setting up properties
    level = property(_get_level, _set_level)

    @property  # alternative syntax for property
    def score(self):
        """Score property."""

        return self._score

    @score.setter  # name of property
    def score(self, score):
        """"""
        self._score = score

    def __str__(self):
        """Show attributes."""

        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
