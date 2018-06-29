import shelve
import random

print(dir())
print()
print(dir(shelve))  # show objects/methods from shelve module
print("=" * 40)

for m in dir(__builtins__):
    print(m)
print("=" * 40)

for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

# brings up help info and link to docs
help(random.gauss)
