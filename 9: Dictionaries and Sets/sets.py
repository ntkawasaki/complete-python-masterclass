# # two ways to create sets
# farm_animals = {"sheep", "cow", "chicken", "hen"}
# print(farm_animals)
# for animal in farm_animals:
#     print(animal.title())
#
# print("=" * 40)
#
# wild_animals = set(["lion", "tiger", "elephant", "panther", "monkey"])
# print(wild_animals)
# for wild_animal in wild_animals:
#     print(wild_animal.title())
#
# print("=" * 40)
#
# # add to sets
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# # must use set function for creating empty set, or will make a dictionary
# empty_set = set()
# empty_broken_set = {}
# empty_set.add("a")
# empty_broken_set.add("a")  # will error because this is a dict, no add() method

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 9, 16, 25)
# squares = set(squares_tuple)  # turns into a set
# print(squares)
# print(len(squares))
#
# # union() and intersection() or &
# # will add 9 and 25 to even only
# print(even.union(squares))
# print(squares.union(even))  # same output
# print(len(even.union(squares)))
#
# print("=" * 40)
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# print("=" * 40)
# print(sorted(even))
# print(sorted(squares))
#
# # difference
# print("even minus squares:")
# print(even.difference(squares))
# print(even - squares)
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# # removed squares from even
# even.difference_update(squares)  # squares is the param, even is being acted on
#
# print("=" * 40)
# print(even)
# print(squares)
#
# # symmetric difference
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
#
# # discard and remove
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error, does nothing
# print(squares)
# # squares.remove(8)  # will throw error if value not existing
# # could test with
# try:
#     squares.remove(8)
# except KeyError:
#     print("The number 8 is not an item in the set.")

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

# issubset() and issuperset()
if squares.issubset(even):
    print("squares is a subset of even")  # all members in squares are contained in even
if even.issuperset(squares):
    print("even is a superset of squares")  # even contains all members of squares

# frozen set
frozen_even = frozenset(range(0, 100, 2))  # immutable
print(frozen_even)
frozen_even.add(3)
