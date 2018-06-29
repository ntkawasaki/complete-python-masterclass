# shopping_list = ["milk", "eggs", "pretzels", "bacon", "spam"]
# for item in shopping_list:
#
#     # continue skips this value
#     if item == "eggs":
#         break
#
#     print("Buy " + item.title())

meal = ["rice", "chicken", "broccoli", "bread", "fruit"]
nasty_food_item = ""  # initialize variable before its used

for item in meal:
    if item == "broccoli":
        nasty_food_item = "broccoli"
        break
else:
    print("I'll have a plate of that, please.")

if nasty_food_item == "broccoli":
    print("Can't I have anything without broccoli on it?")