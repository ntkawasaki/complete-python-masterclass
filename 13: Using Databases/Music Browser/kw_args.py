# **kwargs


# def print_backwards(*args, end=" ", **kwargs):
# def print_backwards(*args, end=" ", **kwargs):
#     kwargs.pop("end", None)
#     for word in args[::-1]:
#         print(word[::-1], end=" ", **kwargs)

def print_backwards(*args, **kwargs):
    end_character = kwargs.pop("end", "\n")
    sep_character = kwargs.pop("sep", " ")

    for word in args[:0:-1]:                            # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)   # print the first word separately
    # print(end=end_character)                          # so we dont need this line


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop("sep", " ")
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "world", "how", "are", "you?", end="\n")
    print("Another string")

print()
print("hello", "world", "how", "are", "you?", end="", sep="\n**\n")
print_backwards("hello", "world", "how", "are", "you?", end="", sep="\n**\n")
print("=" * 10)

