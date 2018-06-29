i = 0

while i < 10:
    print("i is now {}.".format(i))
    i += 1

available_exits = ["east", "north", "south", "west"]
chosen_exit = input("Please choose a direction: ")

while chosen_exit not in available_exits:
    print("Sorry, that direction is not available")
    chosen_exit = input("Please choose another direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
else:
    print("Great job getting out!")





