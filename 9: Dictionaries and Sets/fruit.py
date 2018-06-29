fruit = {"orange": "a sweet, orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "s small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit please?"}
print(veg)

# update() method merges fruit into veg
# not a new object
veg.update(fruit)
print(veg)
print()

# creates a new dictionary, old dictionaries not modified
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)