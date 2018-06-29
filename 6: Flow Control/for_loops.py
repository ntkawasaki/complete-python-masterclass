# for i in range(1, 21):
#     print("i is now {}".format(i))

number = "9,333,455,768,234"
cleaned_number = ""

# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         cleaned_number = cleaned_number + number[i]  # concatenation of strings

# through a sequence of values
for char in number:
    if char in "0123456789":
        cleaned_number = cleaned_number + char

new_number = int(cleaned_number)
print("The new number is: {}.".format(new_number))

for state in ["not pinin'", "no more", "sad", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    # print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {0}.".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} = {2}".format(j, i, i * j), end="\t")
    # print("===============")
    print("")