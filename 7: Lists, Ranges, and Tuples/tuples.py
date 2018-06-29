# tuples are immutable, can't be altered or appended to
# parenthesis are not necessary, only to resolve ambiguity
# returned in brackets

# t = "a", "b", "c"
# x = ("a", "b", "c")  # using brackets is best practice
# print(t)
# print(x)
#
# print("a", "b", "c")
# print(("a", "b", "c"))  # to print a tuple explicitly include parenthesis

# tuples can put multiple data types on same line
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda Way", 2011
metallica = "Ride the Lightening", "Metallica", 1984

# print(metallica)
# print(metallica[0])  # print one part of tuple
# print(metallica[1])
# print(metallica[2])

# cant change underlying tuple, immutable object
# metallica[0] = "Master of Puppets"
# ca get around this like this though
imelda = imelda[0], "Emilda Way", imelda[2]
# python also evaluates the right side of this expression first, then assigns it to a new variable "imelda"
# creates a new tuple
print(imelda)

# can alter a list though
metallica2 = ["Ride the Lightening", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
print()

# metallica2.append("Rock")
# title, album, year = metallica2
# print(title)
# print(album)
# print(year)
# will draw a too many values to unpack error because not enough variables assigned

# unpacking the tuple, extract values from and assign to variables
title, album, year = imelda
print(imelda)
print("Title: {}".format(title))
print("Album: {}".format(album))
print("Year: {}".format(year))

# tuples don't have an append() method
imelda.append("Rock")

# notes
# lists are intended to hold objects of the same type, tuples not necessarily
# tuples not changing can protect code against bugs

