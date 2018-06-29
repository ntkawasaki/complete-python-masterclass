# ip_input = input("Please enter an IP Address: ")
# print(ip_input.count("."))

# parrot_list = ["not pinin", "no more", "stiff", "bereft of life"]
# parrot_list.append("a norweigian blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# # numbers.sort()  # will not return result, works on existing object, doesnt create new object
# numbers_sorted = sorted(numbers)
#
# print(numbers)
# print(numbers_sorted)
#
# if numbers == numbers_sorted:
#     print("The lists are equal")
# else:
#     print("The lists are not equal")
#
# if numbers_sorted == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")

# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("they are equal")
#
# # makes string into a parsed list
# print(list("the lists are equal"))
#
# even = [2, 4, 6, 8]
# another_even = list(even)  # now this is its own list
# print(another_even == even)  # will return true, contents the same
# print(another_even is even)  # will return false
# another_even.sort(reverse=True)
#
# print(even)
# print(another_even)

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# # makes a list of both lists combined
# numbers = [even, odd]
# print(numbers)
#
# for number_set in numbers:
#     print(number_set)
#
#     for num in number_set:
#         print(num)

# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
# print(menu)
print()

# meals without spam
for meal in menu:
    if not "spam" in meal:
        print("Ingredients: ")
        for ingredient in meal:
            print(ingredient.title())



