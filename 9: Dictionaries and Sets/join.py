# my_list = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "1234567890"
#
# # don't need a loop for join()
# new_string = ", ".join(my_list)
# print(new_string)
#
# letters_string = ", ".join(letters)
# print(letters)
#
# numbers_string = " mississippi ".join(numbers)
# print(numbers_string)

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:

    # initialize variables
    # loops through available directions based on current location
    # for direction in exits[loc].keys():
    #     available_exits += direction + "/"

    # this method is better
    available_exits = ", ".join(exits[loc].keys())

    # prints description of current location
    print(locations[loc])

    if loc == 0:
        break

    print("Available exits are: " + available_exits)
    direction = input("Where would you like to go? ")
    print()

    if direction in exits[loc]:
        # sets location to corresponding loc based on key
        loc = exits[loc][direction]
    else:
        print("Im sorry, you cannot go in that direction.")