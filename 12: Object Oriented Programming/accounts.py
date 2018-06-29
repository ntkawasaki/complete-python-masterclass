# accounts to hold money!
import datetime
import pytz


class Account:
    """A simple account class with balance."""

    @staticmethod  # static method shared by all instances of a class, self not used
    def _current_time():
        """Record time. """
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        """Initialize attributes."""

        self._name = name
        self._balance = balance
        self._transation_log = [(Account._current_time(), balance)]
        print("Account created for: " + name.title())
        self.show_balance()

    def deposit(self, amount):
        """Add amount to balance."""

        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transation_log.append((Account._current_time(), amount))  # with static method use class not self

    def withdraw(self, amount):
        """Subtract amount from balance."""

        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transation_log.append((Account._current_time(), -amount))
        else:
            print("\nThe amount must be greater than 0 and less than your account balance.")
        self.show_balance()

    def show_balance(self):
        """Display accounts current balance."""

        print("Balance is {}.".format(self._balance))

    def show_transactions(self):
        """Display transaction logs."""

        for date, amount in self._transation_log:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    my_account = Account("Noah", 0)

    my_account.deposit(100)
    my_account.withdraw(50)
    my_account.withdraw(20000)
    my_account.show_transactions()

    someone = Account("Someone", 900)
    someone._balance = 800
    someone.deposit(100)
    someone.withdraw(400)
    someone.show_transactions()
    print(someone.__dict__)

