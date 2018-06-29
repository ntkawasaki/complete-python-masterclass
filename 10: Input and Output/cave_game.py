import shelve

# manual open
locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")

loc = "1"  # shelves need strings as keys
while True:
    available_exits = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc == "0":
        break
    else:
        all_exits = locations[loc]["exits"].copy()
        all_exits.update(locations[loc]["named_exits"])

    direction = input("Available exits are " + available_exits + " ").upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break

    if direction in all_exits:
        loc = all_exits[direction]
    else:
        print("You cannot go in that direction")

# manual close
locations.close()
vocabulary.close()
