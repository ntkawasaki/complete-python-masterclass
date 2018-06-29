# write a small program to ask for a name and age
# check if the person is right age to go to a
# 18-30 holiday party, if they are welcome
# welcome them, if not, politely say they can't go
print()
print("Welcome, to Sigma Chi's Holiday Party!")

name = input("Please tell me your name: ")
age = int(input("And your age? "))

if 17 < age < 31:
    print("Welcome to the party, {0}!".format(name.title()))
else:
    print("I'm sorry {0}, but the age limit is between 18 and 30.".format(name.title()))