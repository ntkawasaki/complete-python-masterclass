# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# keys are locations, values are dictionaries with directions
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocab = {"QUIT": "Q",
         "NORTH": "N",
         "SOUTH": "S",
         "EAST": "E",
         "WEST": "W"}

# print(locations[0].split())  # splits into a list of all words
# print(locations[3].split(","))  # splits based on the comma into two lists
# print(" ".join(locations[0].split()))  # splits the text by spaces, then rejoined

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())

    # prints description of current location
    print(locations[loc])

    if loc == 0:
        break

    print("Available exits are: " + available_exits)
    direction = input("Where would you like to go? ").upper()
    print()

    # parse user input with vocab dictionary, if needed
    if len(direction) > 1:  # length longer than one letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocab:
                direction = vocab[word]
                break

    if direction in exits[loc]:
        # sets location to corresponding loc based on key
        loc = exits[loc][direction]
    else:
        print("Im sorry, you cannot go in that direction.")
