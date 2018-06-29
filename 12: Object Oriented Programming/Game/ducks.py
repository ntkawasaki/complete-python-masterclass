# Composition
class Wing(object):
    """Wing."""

    def __init__(self, ratio):
        """Initialize attributes."""
        self.ratio = ratio

    def fly(self):
        """Fly."""

        if self.ratio > 1:
            print("weee this is fun!")
        elif self.ratio == 1:
            print("this is hard work, but im flying.")
        else:
            print("I think ill just walk..")


class Duck(object):
    """Ducks."""

    def __init__(self):
        """Initialize attributes."""

        self._wing = Wing(1.8)

    def walk(self):
        """Walk."""
        print("Waddle waddle waddle.")

    def swim(self):
        """Swim."""
        print("Come on in, the water is lovely.")

    def quack(self):
        """Quack."""
        print("Quack quack.")

    def fly(self):
        """Fly."""
        self._wing.fly()  # now has a wing object, which can use Wing's fly() method. This is composition.


class Penguin(object):
    """Penguin class."""

    def walk(self):
        """Walk."""
        print("Waddle waddle, I waddle too.")

    def swim(self):
        """Swim."""
        print("Come on in, its a bit chilly this far South.")

    def quack(self):
        """Quack."""
        print("Are you avin a larf? Im a penguin!")


# def test_duck(duck):
#     """Test Duck class."""
#
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":

    donald = Duck()
    donald.fly()
    # test_duck(donald)
    #
    # percy = Penguin()  # penguin passes the duck_test, as far as python is concerned, percy is a Duck
    # test_duck(percy)
