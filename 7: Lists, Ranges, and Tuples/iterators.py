string = "1234567890"

# for char in string:
#     print(char)

# # this is what a for loop implicitly does
# # uses next until it sees a stop
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather than counting the number of items in the list.

shopping_list = ["eggs", "granola", "frozen chicken", "shrimp", "greek yogurt", "milk"]
list_iterator = iter(shopping_list)

print(list_iterator)
for i in range(0, len(shopping_list)):
    print(next(list_iterator))

# same
for item in shopping_list:
    print(item)