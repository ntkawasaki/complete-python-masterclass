import random


class Enemy:
    """Enemy class."""

    def __init__(self, name="Enemy", lives=1, hit_points=0):
        """Initialize attributes."""

        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        """Subtract damage from hit points."""

        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{} took {} points in damage and has {} remaining.".format(self._name, damage, self._hit_points))
        else:
            self._lives -= 1
            print("{} died.".format(self._name))
            if self._lives > 0:
                print("{0._name} respawned and has {0._lives} lives remaining.".format(self))
            else:
                print("{0._name} is out of lives.".format(self))
                self._alive = False

    def __str__(self):
        """Return a string with enemy information."""

        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}.".format(self)


class Troll(Enemy):
    """Trolls take 23 hit_points"""

    def __init__(self, name):  # means name is a required parameter now
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        """Grunt method."""

        print("Me {0._name}, {0._name} stomp you.".format(self))


class Vampire(Enemy):
    """Vampires have 3 lives and take 12 hit_points."""

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        """Vampires have a 1 in 3 chance to dodge an attack."""

        if random.randint(1, 3) == 3:
            print("*** {0._name} dodges ***".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        """Overridden Enemy method."""

        if not self.dodges():
            super().take_damage(damage=damage)
        else:
            pass


class VampireKing(Vampire):
    """Vampire Kings take damage divided by 4, and can take 140 hit_points."""

    def __init__(self, name):
        super().__init__(name)  # calls Vampire __init__, which calls Enemy __init__
        self._hit_points = 140

    def take_damage(self, damage):
        """Take 1/4 damage dealt."""

        super().take_damage(damage // 4)  # makes to integer
