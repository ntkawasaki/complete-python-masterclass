# challenge
import sys

# print("This program will calculate any number divided by another number\n")
#
# first = input("Enter a number: ")
# second = input("Enter another number: ")
#
#
# def divide():
#     return int(first)/int(second)
#
#
# try:
#     print(divide())
# except ZeroDivisionError:
#     print("Zero Division Error: You cannot divide by zero.")
# except ValueError:
#     print("Value Error: the numbers must be integers.")
# except EOFError:
#     sys.exit(0)


# instructor solution
def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        except:  # should be ValueError
            print("Invalid entry, must be an int")
        finally:
            print("\t[The finally clause always executes]")


first_num = get_int("Please enter a number: ")
second_num = get_int("Please enter another number: ")

try:
    print("{} divided by {} is {}".format(first_num, second_num, first_num/second_num))
except ZeroDivisionError:
    print("You cannot divide by zero.")
    sys.exit(2)
else:
    print("Division performed successfully.")
