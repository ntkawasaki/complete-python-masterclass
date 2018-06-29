parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
# slice
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:-2])
# start at 0, go for 6, in steps of 2
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,445,635,990"
print(number[1::4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " "probably")

# can use multiplication on strings
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")




