fruit = {"orange": "a sweet, orange fruit.",
         "apple": "good for making cider",
         "lemon": "yellow and sour",
         "grape": "grown in bunches",
         "watermelon": "nice and juicy",
         "blueberry": "willy wonka",
         "raspberry": "put in greek yogurt"}

# print(fruit)
# print(fruit["lemon"])  # uses keys, not indexes
#
# # to add to a dict
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# # if you assign a value to existing key, will replace original value
# fruit["pear"] = "great with tequila"  # overwrites
# print(fruit)

# # to delete, if you don't specify a key deletes entire dict
# del fruit["lemon"]
# print(fruit)
#
# # clear contents but retain dict to use later
# fruit.clear()

# # key does not exist error
# print(fruit["tomato"])

# print(fruit)
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We dont have a {}".format(dict_key))  # this way defines a default value
#     print(description)
#     # if dict_key in fruit:
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("We dont have a {}".format(dict_key))

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is a " + fruit[snack])
#     print("=" * 40)

# # keys() returns keys from dict
# ordered_keys = list(fruit.keys())
# # alpha sort
# ordered_keys.sort()
#
# ordered_keys = sorted(fruit.keys())
#
# for key in ordered_keys:
#     print(key + ": " + fruit[key])
# print()
#
# # unsorted without using keys()
# for f in fruit:
#     print(f + ": " + fruit[f])
# print()
#
# # values() less efficient than keys()
# for val in fruit.values():
#     print(val)
# print()

# fruit_keys = fruit.keys()
# print(fruit_keys)
#
# fruit["tomato"] = "not good with icecream"
# print(fruit_keys)
# print(fruit.values())

print(fruit)
print()
print(fruit.items())
print()
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
print()

print(dict(f_tuple))
