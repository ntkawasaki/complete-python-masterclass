# write a block of code once, can call whenever
# easy to maintain if you see you keep rewriting the same code
# print function written in C


def python_food():
    """ Prints pythons favorite food! """

    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# center_text() has same signature as print() means they have same params
def center_text(*args, sep=" "):  # parameter = text
    """
    Prints centered text.

    Optional arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

    :returns string
    """

    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centered", mode="w") as centered_file:

# calling function
s1 = center_text("spam and eggs", 55, 4444, sep="\t")
s2 = center_text("spam, spam and eggs")
s3 = center_text("wingsuit god")
s4 = center_text("swift", 2, "black")
print(s1)
print(s2)
print(s3)
print(s4)

with open("test_file", mode="w") as test_file:

    s1 = center_text("spam and eggs", 55, 4444, sep="\t")
    s2 = center_text("spam, spam and eggs")
    s3 = center_text("wingsuit god")
    print(s1, file=test_file)
    print(s2, file=test_file)
    print(s3, file=test_file)

    # without assigning variable
    print(center_text("swift", 2, "black"), file=test_file)

