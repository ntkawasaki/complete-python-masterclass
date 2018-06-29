print()

name = input("Please tell me your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if not (age < 18):
    print("You are old enough to vote.")
    print("Please put an X in the box.")
else:
    print("Please come back in {0} years".format(18 - age))

# print("Please guess a number between 1 and 10.")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher.")
#     else:
#         print("Please guess lower.")
#     guess = int(input())
#
#     if guess == 5:
#         print("Well done!")
#     else:
#         print("Sorry, you are wrong again.")
# else:
#     print("Nice, first try!!!")

# age = int(input("How old are you? "))

# if (age >= 16) and (age <= 65):
# if 15 < age < 66:
#     print("Have a great day at work!")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time!")
# else:
#     print("Have a good day at work!")

# x = input("Please enter some text: ")
#
# if x:
#     print("You entered {0}.".format(x))
# else:
#     print("You did not enter anything.")
#
# print(not True)
# print(not False)