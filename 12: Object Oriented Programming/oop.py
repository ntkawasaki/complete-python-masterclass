# object oriented programming intro


class Kettle(object):

    # class attribute shared by all instances
    power_source = "electricity"

    def __init__(self, make, price):  # make and price are attributes
        """Initialize attributes."""

        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        """Turn on kettle."""

        self.on = True


# create an instance of Kettle()
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

# another instance of Kettle()
hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = ${}, {} = ${}.".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# can use attributes in replacement fields
print("Models: {0.make} = ${0.price}, {1.make} = ${1.price}.".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# use class def to call method, instance as param
Kettle.switch_on(kenwood)
print(kenwood.on)

print("=" * 40)

# can create attribute for instance after made
kenwood.power = 85
print(kenwood.power)

# class attribute
print("Switch to atomic power")
Kettle.power_source = "atomic"
hamilton.power_source = "gas"

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
