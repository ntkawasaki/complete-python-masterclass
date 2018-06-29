# # range is its own object type in python
# print(range(100))
#
# my_list = list(range(10))
# print(my_list)
#
# even = list(range(0, 100, 2))
# odd = list(range(1, 100, 2))
#
# print(even)
# print(odd)
#
# # use same amount of memory
# range(0, 10)
# range(0, 100)

# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index("e"))
# print(my_string[4])
#
# small_decimals = range(0, 10)
# print(small_decimals)
# print(small_decimals.index(3))
#
# # will only be range, not a list
# odd = range(1, 10000, 2)
# print(odd)
# print(odd[985])  # the 985th index in odd
#
# sevens = range(7, 100000, 7)
# x = int(input("Please enter a positive number, less than 1000000: "))
#
# if x in sevens:
#     print("{} is divisible by seven!".format(x))
# else:
#     print("{} is not divisible by seven".format(x))

# print(small_decimals)
#
# adds every other step part to range
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

# the same thing
for i in range(3, 40, 3):
    print(i)

# test
print(my_range == range(3, 40, 3))