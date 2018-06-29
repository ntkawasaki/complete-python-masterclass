# like a dictionary stored in a file, uses keys and values
# persistent dictionary
# values pickled when saved, don't use untrusted sources

import shelve

# open a shelf like its a file
# with shelve.open("shelf_test") as fruit:  # makes a shelf_test.db file
#     fruit["orange"] = "a sweet, orange fruit"
#     fruit["apple"] = "good for making cider"
#     fruit["lemon"] = "a sour, yellow fruit"
#     fruit["grape"] = "a small, sweet fruit grown in bunches"
#     fruit["lime"] = "a sour, green citrus fruit"

# when outside of the with, it closes the file
# print(fruit)  # prints as a shelf and not a dictionary

# to do this with manual open and closing
fruit = shelve.open("shelf_test")
# fruit["orange"] = "a sweet, orange fruit"
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour, yellow fruit"
# fruit["grape"] = "a small, sweet fruit grown in bunches"
# fruit["lime"] = "a sour, green citrus fruit"

# # change value of "lime"
# fruit["lime"] = "goes great with tequila!"
#
# for snack in fruit:
#     print(fruit[snack])

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# alpha sorting keys
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])
#
# fruit.close()  # remember to close

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()