# * means it expects an unpacked tuple
def average(*args):
    """Return arithmetic average of numbers."""

    print(type(args))
    print("args is {}.".format(args))  # returns tuple
    print("*args is", *args)           # returns unpacked tuple

    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    return args


message_tuple = build_tuple("hello", "world", "how", "are", "you?")
print(type(message_tuple))
print(message_tuple)

numbers_tuple = build_tuple(1, 2, 3, 4, 5, 6, 7, 8)
print(type(numbers_tuple))
print(numbers_tuple)