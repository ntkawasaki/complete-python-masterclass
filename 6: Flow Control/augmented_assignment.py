number = "9,223,372,036,854,775,807"
cleaned_number = ""  # initialize all variables

for i in range(0, len(number)):
    if number[i] in "0123456789":
        # cleaned_number = cleaned_number + number[i]
        cleaned_number += number[i]  # augmented assignment

new_number = int(cleaned_number)
print("The new number is {}.".format(cleaned_number))

x = 23
print(x)

x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = "Good "
greeting += "morning! "
greeting *= 5
print(greeting)