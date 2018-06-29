a_string = "This is\na string split\t\t and tabbed"
print(a_string)

raw_string = r"This is\na string split\t\t and tabbed"
print(raw_string)

b_string = "This is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "This is a backslash \followed by some text"
print(backslash_string)

backslash_string = "This is a backslash \\followed by some text"
print(backslash_string)

error_string = r"This string ends with \\"